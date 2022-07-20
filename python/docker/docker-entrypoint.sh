#!/bin/bash
#

# some more ls aliases
# alias ll='ls -lhF'
# alias la='ls -A'
# alias l='ls -CF'
# alias c='clear'
# alias ..="cd .."

# start sshd
# service ssh start
mkdir -p /run/sshd
/usr/sbin/sshd &

exec "$@"