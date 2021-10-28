#!/bin/bash

con_name="web1"
data_vol="/home/yinkai/Projects/docker_skills/web1/html/"
log_dir="/home/yinkai/Projects/docker_skills/web1/logs/"
ngx_conf="/home/yinkai/Projects/docker_skills/web1/conf/"


function start {
	sudo docker container run --name ${con_name} \
		-P -d --rm -p 8080:80 \
		-v ${log_dir}:/var/log/nginx/ \
		-v ${data_vol}:/usr/share/nginx/html/ \
		-v ${ngx_conf}:/etc/nginx/ \
		nginx:latest > /dev/null
}


function stop {
	sudo docker container stop ${con_name} > /dev/null
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


if [ -z "$1" ]; then
	echo -e "Please input argument (start|stop|restart). "
    exit 5
elif [ $1 == 'start' ]
then
	start
	print_status
elif [ $1 == "stop" ]
then
	stop
elif [ $1 == "restart" ]
then
	stop
	print_status
	start
	print_status
else
	echo "Error Arg: $1"
fi
