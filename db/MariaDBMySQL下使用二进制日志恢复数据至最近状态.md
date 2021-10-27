# MariaDB / MySQL下使用二进制日志恢复数据

## 原理介绍

### 备份分类

按备份形式，数据库备份分为：

​	完全备份：备份完整数据集。不依赖其他备份，备份文件较大；

​	增量备份：只备份自上一次备份以来的新增部分。恢复数据时须按照备份的顺序依次恢复，每个增量备份文件都依赖其前期的备份，当之前的某个备份文件出错时会导致其后的备件不可用；

​	差异备份：只备份自上一次完全备份以来至当前的增量。恢复数据时先恢复完全备份，在此基础上再恢复差异备份。

### 二进制日志介绍

1. 二进制日志记录了对数据库详细的增、删、改操作过程（SQL语句），可以使用二进制日志来恢复数据。
2. 二进制日志的启用需要依赖log_bin和sql_log_bin这两个系统变量。sql_log_bin用于临时启用或禁用二进制日志，不能在配置文件中定义；log_bin用于永久启用或禁用二进制日志，只能在配置文件中定义。这两个系统变量，只要有一个没有启用，则二进制日志就不会启用。
3. 二进制日志文件应该单独存放，不与数据库文件存在同一磁盘。

### 启用二进制日志

**查看是启用了二进制日志：**

```sql
mariadb root@localhost:hellodb> SHOW VARIABLES LIKE '%log_bin';		-- 查看是启用了二进制日志
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
| sql_log_bin   | ON    |
+---------------+-------+
```

若没有启用，修改MariaDB的配置文件，使之启用：

```shell
$ vim mariadb.conf.d/50-server.cnf
[mysqld]
log_bin         = /mydata/logs/mysqld-binlog
```

查看当前使用的二进制日志文件

```sql
mariadb root@localhost:hellodb> SHOW MASTER STATUS;
+----------------------+----------+--------------+------------------+
| File                 | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+----------------------+----------+--------------+------------------+
| mysqld-binlog.000001 | 332      |              |                  |
+----------------------+----------+--------------+------------------+
```

**MariaDB/MySQL数据库启用二进制日志文件，定期执行完全备份。当数据库出现问题时，先使用最近的完全备份进行恢复，再在二进制日志文件中找出自该完全备份之后至出现问题时的更新，并执行这些更新即可恢复数据至最近状态。此方法使用了完全备份 + 二进制日志的方式进行数据恢复。**

## 备份

**备份工具：mysqldump**

Dumping structure and contents of MySQL databases and tables.
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases
OR     mysqldump [OPTIONS] --system=[SYSTEMOPTIONS]]

**-A, --all-databases**		Dump all the databases. This will be same as --databases with all databases selected.

**-B, --databases**			Dump several databases. Note the difference in usage; in this case no tables are given. All name arguments are regarded as database names. 'USE db_name;' will be included in the output.

**--master-data[=#]**  	This causes the binary log position and filename to be appended to the output. If equal to 1, will print it as a CHANGE MASTER command; if equal to 2, that command will be prefixed with a comment symbol. 



1. 备份数据库，并在备份脚本中记录二进制日志的位置:

```shell
$ mysqldump -uroot -pmydbpass -h172.17.0.2 -B hellodb --master-data=2 > hellodb_bak.sql
$ grep -i master_log hellodb_bak.sql 
-- CHANGE MASTER TO MASTER_LOG_FILE='mysqld-binlog.000001', MASTER_LOG_POS=332;
```

2. 更新数据库内容：

```sql
mariadb root@localhost:hellodb> DELETE FROM test WHERE id = (SELECT MAX(id) FROM test);
mariadb root@localhost:hellodb> INSERT INTO test (id, firstname, lastname) VALUES (3,'a', 'a1'), (4, 'b', 'b1');
mariadb root@localhost:hellodb> SHOW MASTER LOGS;		-- 查看二进制日志文件位置。由此可见，位置已经从之前的332偏移至871
+----------------------+-----------+
| Log_name             | File_size |
+----------------------+-----------+
| mysqld-binlog.000001 | 871       |
+----------------------+-----------+
```

## 模拟数据库故障

删除数据库：

```sql
mariadb root@localhost:hellodb> DROP DATABASE hellodb;
mariadb root@localhost:(none)> SHOW MASTER LOGS;	-- 再次查看二进制日志位置
+----------------------+-----------+
| Log_name             | File_size |
+----------------------+-----------+
| mysqld-binlog.000001 | 1004      |
+----------------------+-----------+
```

## 恢复

1. 停用二进制日志（若生产中，此时要维护数据库，应立即断开网络连接，使数据库处于脱机状态）：

```sql
mariadb root@localhost:(none)> SET sql_log_bin=OFF;
mariadb root@localhost:(none)> SHOW VARIABLES LIKE '%log_bin';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
| sql_log_bin   | OFF   |
+---------------+-------+
```

2. 使用之前的备份脚本导入数据：

```sql
MariaDB [hellodb]> SOURCE ~/Projects/docker_volumes/mydata/logs/backup/hellodb_bak.sql
#注意：此时只能在登录到RDBMS上，使用SOURCE命令导入，不能在文件系统上执行导入（$ mysql -uroot -p < hellodb_bak.sql），否则导入过程会记录到二进制日志
```

3. 查看备份数据时，使用的二进制日志文件及位置：

```shell
$ grep MASTER_LOG_POS hellodb_bak.sql 
-- CHANGE MASTER TO MASTER_LOG_FILE='mysqld-binlog.000001', MASTER_LOG_POS=332;
```

4. 找出问题SQL语句的位置：

```shell
# mysqlbinlog --start-position=332 mysqld-binlog.000001 | grep -B 15 -i 'drop database hellodb'
COMMIT/*!*/;
# at 871
#210718 16:19:31 server id 1  end_log_pos 913 CRC32 0xd56b0a34  GTID 0-1-3 ddl
/*!100001 SET @@session.gtid_seq_no=3*//*!*/;
# at 913		# DROP DATABASE hellodb 出现在二进制日志的位置
#210718 16:19:31 server id 1  end_log_pos 1004 CRC32 0x05ba3301         Query   thread_id=33    exec_time=0     error_code=0
SET TIMESTAMP=1626625171/*!*/;
SET @@session.pseudo_thread_id=33/*!*/;
SET @@session.foreign_key_checks=1, @@session.sql_auto_is_null=0, @@session.unique_checks=1, @@session.autocommit=1, @@session.check_constraint_checks=1, @@session.sql_if_exists=0/*!*/;
SET @@session.sql_mode=1411383296/*!*/;
SET @@session.auto_increment_increment=1, @@session.auto_increment_offset=1/*!*/;
/*!\C utf8mb4 *//*!*/;
SET @@session.character_set_client=45,@@session.collation_connection=45,@@session.collation_server=45/*!*/;
SET @@session.lc_time_names=0/*!*/;
SET @@session.collation_database=DEFAULT/*!*/;
DROP DATABASE hellodb
```

5. 使用mysqlbinlog，从二进制日志文件中截取要恢复的SQL语句至脚本文件中（此例中为332至913）：

```shell
# mysqlbinlog --start-position=332 --stop-position=913 mysqld-binlog.000001 > incr.sql
```

6. 在数据库数据中执行截取的二进制文件 ：

```sql
MariaDB [hellodb]> source ~/Projects/docker_volumes/mydata/logs/backup/incr.sql
```

7. 验证数据：

```sql
MariaDB [hellodb]> SELECT * FROM test;
+----+-----------+----------+-------------+
| id | firstname | lastname | phone       |
+----+-----------+----------+-------------+
|  3 | a         | a1       | NULL        |
|  4 | b         | b1       | NULL        |
|  2 | Bai       | Na       | 15810697243 |
|  1 | Li        | Yinkai   | 15810697243 |
+----+-----------+----------+-------------+
```

8. 恢复记录二进制日志文件 ：

```sql
MariaDB [hellodb]> SET sql_log_bin=ON;
MariaDB [hellodb]> SHOW VARIABLES LIKE '%log_bin';  
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
| sql_log_bin   | ON    |
+---------------+-------+
```

