FROM busybox:latest
LABEL Maintainer="Yinkai <yinkai.li@foxmail.com>" app="httpd"

ENV WEB_DOC_ROOT="/data/web/html/"

RUN mkdir -p ${WEB_DOC_ROOT} && \
    echo '<h1>Busybox httpd server.</h1>' > ${WEB_DOC_ROOT}index.html

# CMD [ "executable" ]
# CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
CMD ["/bin/httpd", "-f", "-h ${WEB_DOC_ROOT}"]
