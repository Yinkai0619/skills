/*
参数类型：
	IN: 传入参数给存储过程
	OUT：从存储过程传出
	INOUT：既可传入又可传出的参数
*/

-- 存储过程：查询当前时间
CREATE PROCEDURE showTime()
BEGIN
	SELECT now();
END

CALL showTime;


-- 存储过程：通过调用存储过程传值来查表
CREATE PROCEDURE selectById(IN uid SMALLINT UNSIGNED)
BEGIN
	SELECT * FROM testdb1.employee WHERE id = uid;
END

CALL selectById(1);


-- 存储过程：实现数值累加
CREATE PROCEDURE doRepeat(n INT)
BEGIN
	SET @i = 0;
	SET @sum = 0;
	REPEAT SET @sum = @sum + @i; SET @i = @i + 1;/**/
	UNTIL @i > n END REPEAT;
END

CALL doRepeat(100); 
SELECT @sum;


-- 存储过程：删除emplyoee表中指定ID的人员，并输出删除的记录行数。
-- 包含一个IN参数和一个OUT参数。调用时传入删除的ID，保存被修改的行数值（用@line变量来接收）。
CREATE PROCEDURE deleteById(IN uid SMALLINT UNSIGNED, OUT num SMALLINT UNSIGNED)
BEGIN
	DELETE FROM testdb1.employee WHERE id = uid;
	SELECT row_count() INTO num;	-- row_count: 上条指令影响的行数
END

-- SELECT * FROM employee;
CALL deleteById(4,@line);
SELECT @line;


-- 列出已有的存储过程和函数：
SHOW PROCEDURE STATUS;

-- 列出以“pro_”开头的存储过程：
SHOW PROCEDURE STATUS LIKE 'pro_%';

-- 查看指定存储过程的内容和创建信息：
SHOW CREATE PROCEDURE pro_testlog;


-- 列出已有函数：
SHOW FUNCTION STATUS;

-- 删除指定函数：
DROP FUNCTION deleteById;


-- 触发器

-- 创建学生信息表和学生统计表
CREATE TABLE student_info (
	stu_id INT(11) NOT NULL AUTO_INCREMENT,
	stu_name VARCHAR(255) DEFAULT NULL,
	PRIMARY KEY (stu_id)
);

CREATE TABLE student_count (
	stu_count INT(11) DEFAULT 0
);

INSERT INTO student_count VALUES (0);
SELECT * FROM student_count;
SELECT * FROM student_info;

-- 查看触发器：
SHOW TRIGGERS


-- 创建触发器：
-- 当向student_info表中INSERT数据时，student_count表加1，DELETE数据时student_count减1
CREATE TRIGGER trigger_student_count_insert
AFTER INSERT 
ON student_info FOR EACH ROW
UPDATE student_count SET stu_count = stu_count + 1;

CREATE TRIGGER trigger_student_count_delete
AFTER DELETE 
ON student_info FOR EACH ROW 
UPDATE student_count SET stu_count = stu_count - 1;

-- 测试触发器：
INSERT INTO student_info (stu_name) VALUES("Yinkai"), ("Nana");
SELECT * FROM student_info ;
SELECT * FROM student_count;
DELETE FROM student_info WHERE stu_id = 2;

-- 删除触发器
SHOW TRIGGERS;
DROP TRIGGER trigger_student_count_delete;











