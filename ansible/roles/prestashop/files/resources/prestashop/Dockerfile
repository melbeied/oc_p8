FROM prestashop/prestashop-git:latest
RUN apt-get update -y
RUN apt-get install -y vim

# RUN apt-get install -y --no-install-recommends iproute2 php7.3-cli php7.3-common \
#      php7.3-opcache php7.3-json libapache2-mod-php7.3 \
#      ca-certificates && \
#     apt-get autoremove -y && \
#     rm -rf /var/lib/apt/lists/* 

#RUN echo "ServerName $(ip route get 8.8.8.8 | awk '{print $NF; exit}')" >> /etc/apache2/apache2.conf

# To run files with the same group as your primary user
RUN groupmod -g 1000 www-data \
  && usermod -u 1000 -g 1000 www-data

COPY /wait-for-it.sh /tmp/
COPY /docker_run_git.sh /tmp/

CMD ["/tmp/docker_run_git.sh"]
