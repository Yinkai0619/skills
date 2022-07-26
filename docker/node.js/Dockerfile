# Description: This is a development environment for Node.js.

FROM node:latest

# LABEL key="value"
# LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>
LABEL Maintainers="Yinkai <yinkai.li@foxmail.com>"

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    apt-get clean && \
    apt update && apt upgrade -y  && \
    apt install -y vim less net-tools iproute2 openssh-server && \
    apt-get autoremove && apt-get clean

# RUN /usr/local/bin/python -m pip install --upgrade pip && \
#     pip3 install ipython --no-cache-dir

RUN echo "root:secret" | chpasswd

RUN sed -i '/#PermitRootLogin/a PermitRootLogin yes' /etc/ssh/sshd_config && \
    sed -i '/#UseDNS no/c UseDNS no' /etc/ssh/sshd_config

RUN echo '' >> ~/.bashrc && \
    echo '# some more ls aliases' >> ~/.bashrc && \
    echo 'alias ll="ls -lhF"' >> ~/.bashrc && \
    echo 'alias la="ls -A"' >> ~/.bashrc && \
    echo 'alias l="ls -CF"' >> ~/.bashrc && \
    echo 'alias c="clear"' >> ~/.bashrc && \
    echo 'alias ..="cd .."' >> ~/.bashrc


EXPOSE 22/tcp 80/tcp 443/tcp

ADD docker-entrypoint.sh /bin/
# cat docker-entrypoint.sh
# #!/bin/bash
# #
# # start sshd
# # service ssh start
# mkdir -p /run/sshd
# /usr/sbin/sshd &
# exec "$@"




CMD [ "node" ]
ENTRYPOINT [ "/bin/docker-entrypoint.sh" ]
# ENTRYPOINT [ "service", "ssh", "start", "&&", "exec '$@'" ]