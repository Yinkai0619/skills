-- 给test表施加读锁：
lock table test read;
-- 释放表锁：
unlock tables;

-- 查看当前数据库系统的DML的事务日志是否自动提交：
SELECT @@autocommit;

-- 列出以"pro_"开头的存储过程：
SHOW PROCEDURE STATUS LIKE 'pro_%';
-- 查看指定存储过程的内容和创建信息：
SHOW CREATE PROCEDURE pro_testlog;

-- 查看当前事务隔离级别：
SELECT @@tx_isolation;

-- 设置当前事务的隔离级别（重启后失效）：
set tx_isolation='READ-UNCOMMITTED';
set tx_isolation='SERIALIZABLE';

SELECT * FROM test t order by id DESC ;


-- 查看当前数据库系统的进程：
show processlist;

-- 杀掉某进程：
kill 14;
