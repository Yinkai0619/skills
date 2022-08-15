#!/bin/bash

docker container run \
    --name mynode --hostname mynode \
    -it \
    --rm \
    -P \
    -v "$PWD":/mydata -w /mydata \
    --network mybr0 --ip 172.27.0.1 \
    mynode:v0.1 "$@"