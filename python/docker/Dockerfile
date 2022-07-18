# Description: This is a development environment for Python.

FROM python:latest

# LABEL key="value"
# LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>
LABEL Maintainers="Yinkai <yinkai.li@foxmail.com>"

RUN apt update && apt upgrade -y && apt-get autoremove; apt-get clean && \
    apt install -y vim

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip3 install ipython --no-cache-dir

