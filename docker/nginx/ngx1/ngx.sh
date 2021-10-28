#!/bin/bash

con_name="ngx1"
vol="$PWD/${con_name}/"
ngx_conf_file="/home/yinkai/Projects/docker_skills/ngx_server/conf/"
ngx_logs="/home/yinkai/Projects/docker_skills/ngx_server/logs/"
cache_dir="/home/yinkai/Projects/docker_skills/ngx_server/cache/"


function start {
	sudo docker container run --name ${con_name} \
		-P --rm -d \
		-v ${ngx_logs}:/var/log/nginx/ \
		-v ${ngx_conf_file}:/etc/nginx/ \
		-v ${cache_dir}:/cache/ \
		nginx:latest &> /dev/null
}


stop(){
	sudo docker container stop ${con_name} > /dev/null 2>&1
	sleep 1
}


# 检查容器运行状态。正在运行返回1, 否则返回0
is_running(){
	[ -z "$(sudo docker container ls -a | grep ${con_name})" ] && echo 0 || echo 1
}


print_status(){
	if [ $(is_running) -eq 0 ] ; then
		echo -e "${con_name} is stoped."
	else
		echo "${con_name} is running."
	fi
}


if [ -z "$1" ]
then
	echo -e "Please input argument (start|stop|restart). "
	exit 5

elif [ $1 == 'start' ]
then
	start
	print_status

elif [ $1 == "stop" ]
then
	stop
	print_status

elif [ $1 == "restart" ]
then
	stop
	print_status
	start
	print_status

else
	echo "Error Arg: $1"
fi
