#!/bin/bash
#

if [ -z "$*" ]; then
	#echo -e "The arguments given are incorrect.\n"
	echo -e "The argument cannot be empty.\n"  
	echo -e "Usage: $(basename $0) [start|stop|restart|[check|status]] [CONTAINERS] \n"
	exit 5
fi


con_args=${@:2}		# 实参中的容器名


function start {
	con_name="$1"
	con_root="/home/yinkai/Projects/docker_skills/elasticsearch/${con_name}"
	data_dir="${con_root}/data/"
	log_dir="${con_root}/logs/"
	conf_dir="${con_root}/conf/"
	ip_addr="10.0.1.$(echo ${con_name} | tr -cd "[0-9]")"	# 取出容器名称中的数字部分作为IP地址, 此处需与elasticsearch.yml配置文件中的地址保持一致

	sudo docker container run --name ${con_name} \
		-P -d --rm \
		-v ${log_dir}:/els/logs \
		-v ${data_dir}:/els/data \
		-v ${conf_dir}:/etc/elasticsearch \
		--network mybr0 \
		--ip ${ip_addr} \
		--hostname ${con_name} \
		--add-host=node01:10.0.1.1 \
		--add-host=node02:10.0.1.2 \
		--add-host=node03:10.0.1.3 \
		elasticsearch:latest > /dev/null
}


function stop {
	sudo docker container stop $1 > /dev/null
	sleep 1
}


# 获取运行中的容器名称列表
get_cons() {
	echo $(sudo docker container ls | awk 'NR>1{print $NF}')
}


# 输出容器当前状态
print_status() {
	ret=$(echo $(get_cons) | grep "$1")
    if [ -z "$ret" ] ; then
            echo -e "$1 is stoped."
    else
            echo "$1 is running."
    fi
}


if [ $1 == 'start' ]	# 启动容器
then
	for c in ${con_args}; do
		start ${c}
		print_status ${c}
	done
	#start $2
	#print_status $2
	exit 0

elif [ $1 == "stop" ]	# 停止容器
then
	if [[ $2 == all || $2 == "" ]]; then
		for c in $(get_cons); do
			stop ${c}
			print_status ${c}
		done
		exit 0

	else
		for c in ${con_args}; do
			stop ${c}
			print_status ${c}
		done
		exit 0
	fi

elif [ $1 == "restart" ]	# 重启容器
then
	for c in ${con_args}; do
		stop ${c}
		print_status ${c}
		start ${c}
		print_status ${c}
	done
	exit 0

elif [ $1 == "check" -o $1 == "status" ]
then
	if [[ -z "$2" || $2 == "all" ]]; then
		sudo docker container ls
	else
		sudo docker container ls -f name=^"$2"$
	fi		
else
	echo "Error Arg: $1"
fi
exit 0
