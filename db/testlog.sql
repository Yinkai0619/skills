use testdb1;

-- 创建一个测试表
CREATE table testlog (
	id int auto_increment primary key,
	name char(10),
	age int default 20
	);
	
-- 创建一个存储过程，向表中插入一些数据
CREATE  PROCEDURE pro_testlog(IN count INT)
BEGIN
	DECLARE i int;
	set i = 1;
	while i < count
	do
		INSERT INTO testlog (name, age) VALUES (concat('Li-', i), i);
		set i = i + 1;
	end while;
END

-- 调用存储过程
CALL pro_testlog(100000);

SELECT COUNT(*) FROM testlog t ; 

-- 创建name字段上的索引
create index index_name on testlog(name(10));
