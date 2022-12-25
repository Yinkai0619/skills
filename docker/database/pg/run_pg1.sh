sudo docker container run --name pg1 --hostname pg1 \
	--rm -d -P \
	-p 127.0.0.1:54321:5432 \
	-v /mnt/dvs/dbs/pg1/:/var/lib/postgresql/data \
	-v /mnt/dvs/mydata/:/mydata \
	-e POSTGRES_PASSWORD=mydbpass \
	postgres:latest
