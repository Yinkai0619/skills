# Description: This is a development environment for Python.

FROM python:latest

# LABEL key="value"
# LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>
LABEL Maintainers="Yinkai <yinkai.li@foxmail.com>"

RUN apt update && apt upgrade -y && apt-get autoremove; apt-get clean && \
    apt install -y vim less net-tools iproute2 openssh-server

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip3 install ipython --no-cache-dir

RUN echo "root:secret" | chpasswd

RUN sed -i '/#PermitRootLogin/a PermitRootLogin yes' /etc/ssh/sshd_config && \
    sed -i '/#UseDNS no/c UseDNS no' /etc/ssh/sshd_config

EXPOSE 22

# CMD [ "service", "ssh", "start" ]
