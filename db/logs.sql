-- 查看InnoDB的事务日志相关的系统变量：
show variables like 'innodb_log%';
/*
innodb_log_buffer_size	16777216
innodb_log_checksums	ON
innodb_log_compressed_pages	ON
innodb_log_file_size	100663296		-- 每个日志文件的大小
innodb_log_files_in_group	1		-- 日志组成员个数
innodb_log_group_home_dir	./		-- 事务日志文件存储位置
innodb_log_optimize_ddl	OFF
innodb_log_write_ahead_size	8192
*/


-- 回收testlog表的事务日志所占用的磁盘空间：
optimize table testlog;

show global variables like 'log_error';

SELECT @@log_error;


-- 查看是否启用慢查询日志：
show variables like 'slow_query_log';

-- 查看慢查询日志路径：
SELECT @@slow_query_log_file;

-- 查看慢查询定义阀值（超过此值的查询语句判定为慢查询）：
SELECT @@long_query_time;

-- 查看是否记录不使用索引的查询语句（即使查询时长未超过慢查询阀值）：
SELECT @@log_queries_not_using_indexes;

DELETE FROM test WHERE id > 5;
SELECT SLEEP(1), id, firstname, lastname FROM test t ;		-- 模拟一个慢查询，每条记录查询时sleep 1秒钟。


-- 使用profile检查慢查询:
-- 1. 检查是否启用profiling：
SELECT @@profiling;

-- 启用profiling:
set profiling=ON ;

-- 2. 模拟一个慢查询：
SELECT SLEEP(1), id, firstname, lastname FROM test t ;

-- 查看并记录慢查询的Query_ID:
show profiles;
/*
+----------+------------+-----------------------------------------+
| Query_ID | Duration   | Query                                   |
+----------+------------+-----------------------------------------+
| 1        | 0.00044987 | select @@profiling                      |
| 2        | 5.00206385 | select sleep(1), id, lastname from test |
+----------+------------+-----------------------------------------+
 * */

-- 查看上一步中，Query_ID为2的查询语句的详细执行过程，在此过程中找出耗时最长的部分：
show profile for query 2;


-- 二进制日志
-- 二进制日志记录了对数据库详细的增、删、改操作过程，可以使用二进制日志来恢复数据。
/*查看是否启用了二进制日志，sql_log_bin用于临时启用或禁用二进制日志，不能在配置文件中定义；log_bin用于永久启用或禁用二进制日志，
 * 只能在配置文件中定义。这两个系统变量，只要有一个没有启用，则二进制日志就不会启用。：*/
show variables like '%log_bin';
/*
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | OFF   |
| sql_log_bin   | ON    |
+---------------+-------+
*/

-- 查看二进制日志的记录格式：
SELECT @@binlog_format;

-- 修改二进制日志文件格式为ROW：
SET binlog_format=ROW ;

-- 查看二进制日志文件及大小，默认每次重启数据库服务时都会生成一个二进制日志文件：
show binary logs; 
/*
+-------------------+-----------+
| Log_name          | File_size |
+-------------------+-----------+
| mysqld-bin.000001 |       329 |
+-------------------+-----------+
*/

-- 查看二进制日志的详细信息：
show master status;
/*
+-------------------+----------+--------------+------------------+
| File              | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+-------------------+----------+--------------+------------------+
| mysqld-bin.000001 | 27678201 |              |                  |
+-------------------+----------+--------------+------------------+
*/

-- 查看二进制日志文件
-- 1. 登陆到mysql后，使用自带的工具查看。从二进志日志文件的329位置处，向后赢取5条记录：
show binlog events in 'mysqld-bin.000001' from 329 limit 5;
-- +-------------------+-----+------------+-----------+-------------+---------------------------------------------------------------------+
-- | Log_name          | Pos | Event_type | Server_id | End_log_pos | Info                                                                |
-- +-------------------+-----+------------+-----------+-------------+---------------------------------------------------------------------+
-- | mysqld-bin.000001 | 329 | Gtid       | 1         | 371         | BEGIN GTID 0-1-1                                                    |
-- | mysqld-bin.000001 | 371 | Intvar     | 1         | 403         | INSERT_ID=6                                                         |
-- | mysqld-bin.000001 | 403 | Query      | 1         | 525         | use `testdb1`; insert into student (name,gender) values('Nana','f') |
-- | mysqld-bin.000001 | 525 | Xid        | 1         | 556         | COMMIT /* xid=25 */                                                 |
-- | mysqld-bin.000001 | 556 | Gtid       | 1         | 598         | GTID 0-1-2                                                          |
-- +-------------------+-----+------------+-----------+-------------+---------------------------------------------------------------------+

-- 使用mysqlbinlog工具，直接从文件系统上读取二进制日志文件：
-- 1). 以位置为标记，从二进制日志文件中读取525至764之间的操作：
-- mysqlbinlog --start-position=525 --stop-position=764 mysqld-bin.000001
-- 2.） 以时间为标记，从二进制日志文件中读取操作：
-- mysqlbinlog  --start-datetime='2021-7-13 14:59:18' --stop-datetime='2021-7-13 15:21:52' mysqld-bin.000001

-- 切换二进制日志文件：
show master logs;
-- +---------------------+-----------+
-- | Log_name            | File_size |
-- +---------------------+-----------+
-- | mysql-binlog.000001 | 2921      |
-- | mysql-binlog.000002 | 441       |
-- | mysql-binlog.000003 | 391       |
-- +---------------------+-----------+
flush logs;    -- 每次执行该命令就会生成一个新的日志文件
show master logs;
-- +---------------------+-----------+
-- | Log_name            | File_size |
-- +---------------------+-----------+
-- | mysql-binlog.000001 | 2921      |
-- | mysql-binlog.000002 | 441       |
-- | mysql-binlog.000003 | 441       |
-- | mysql-binlog.000004 | 391       |
-- +---------------------+-----------+
PURGE BINARY LOGS TO 'mysql-binlog.000003';		-- 删除000003之前的日志文件
show master logs;
-- +---------------------+-----------+
-- | Log_name            | File_size |
-- +---------------------+-----------+
-- | mysql-binlog.000003 | 441       |
-- | mysql-binlog.000004 | 391       |
-- +---------------------+-----------+
RESET MASTER;		-- 重新从开始记录二进制日志
SHOW MASTER LOGS;
-- +---------------------+-----------+
-- | Log_name            | File_size |
-- +---------------------+-----------+
-- | mysql-binlog.000001 | 331       |
-- +---------------------+-----------+




