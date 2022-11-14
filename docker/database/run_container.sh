sudo docker container run --name db1 --hostname db1 \
	--rm -d -P \
	-p 127.0.0.1:33061:3306 \
	-v /mnt/dvs/db/:/var/lib/mysql \
	-v /mnt/dvs/mydata/:/mydata \
	-e MYSQL_ROOT_PASSWORD=mydbpass \
	mariadb:latest

# sudo docker container run --name db1 --hostname db1 \
# 	--rm -d -P \
# 	-p 127.0.0.1:33061:3306 \
# 	-v /mnt/dvs/db/:/var/lib/mysql \
# 	-v /mnt/dvs/mysql_conf/:/etc/mysql \
# 	-v /mnt/dvs/mydata/:/mydata \
# 	-e MYSQL_ROOT_PASSWORD=mydbpass \
# 	mariadb:latest
