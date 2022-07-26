#!/bin/bash
#

# start sshd
# service ssh start
mkdir -p /run/sshd
/usr/sbin/sshd &

exec "$@"