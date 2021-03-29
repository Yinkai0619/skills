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

-- 列出已有函数：
SHOW FUNCTION STATUS;

-- 删除指定函数：
DROP FUNCTION deleteById;
