$ mysqldump -uroot -pmydbpass -h172.17.0.2 -B hellodb > hellodb.sql 	# 备份hellodb数据库。使用-B选项时，可以指定多个数据库，不可指定表；此时将会在导出的SQL脚本文件中添加 CREATE DATABASE语句，否则需要在导入数据时事先创建数据库。
$ mysql -uroot -pmydbpass -h172.17.0.2 < hellodb.sql 	# 恢复数据库


show master logs;
show master status;