FROM youkidearitai/php7-tmcmaker

VOLUME /home/vagrant/media_webroot /var/www/htdocs/cake/app/media_webroot/
EXPOSE 80 80
env APACHE_RUN_USER    www-data
env APACHE_RUN_GROUP   www-data
env APACHE_PID_FILE    /var/run/apache2.pid
env APACHE_RUN_DIR     /var/run/apache2
env APACHE_LOCK_DIR    /var/lock/apache2
env APACHE_LOG_DIR     /var/log/apache2
env LANG               C
ENTRYPOINT ["/usr/sbin/apache2", "-D", "FOREGROUND"]

