FROM debian:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y apache2 apache2-mpm-prefork apache2-dev build-essential autoconf libpq-dev libxml2-dev libicu-dev libdb-dev libjpeg-dev libpng-dev libgif-dev libgd-dev libreadline-dev libgd-dev libgd2-xpm-dev libcurl4-openssl-dev openssl

RUN a2dismod mpm_event && a2enmod mpm_prefork

ADD php-src/ /usr/local/src/
WORKDIR /usr/local/src/
RUN ./configure --with-apxs2=/usr/bin/apxs --enable-mbstring --enable-intl --with-pgsql=/usr/include/postgresql --with-pdo-pgsql --with-gd=/usr/include/ --with-jpeg-dir=/usr/include --with-png-dir=/usr/include/ --with-readline=/usr/include --with-xpm-dir=/usr/include --with-openssl && make && make install && make clean
WORKDIR /usr/local/
RUN rm -rf src/*
RUN apt-get clean

ADD conf/apache2/01-tekitoh-memdhoi.conf /etc/apache2/sites-available/
ADD conf/apache2/02-img-tekitoh-memdhoi.conf /etc/apache2/sites-available/
ADD conf/apache2/php7.conf /etc/apache2/mods-available/
ADD conf/apache2/status.conf /etc/apache2/mods-available/
RUN a2enmod php7 && a2enmod rewrite && a2enmod status
RUN a2ensite 01-tekitoh-memdhoi && a2ensite 02-img-tekitoh-memdhoi

