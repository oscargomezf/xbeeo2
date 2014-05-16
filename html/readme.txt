This directory contains the website you have to download to the directory "/www/var" once installed lighttpd and php:
cgi:

1. Install lighthttpd:

# apt-get install lighttpd

2. Install cgi-php:

# apt-get install php5-cgi

3. Modify the lighttp server config to link php files to the php5-cgi.

# nano /etc/lighttpd/lighttpd.conf

In the area marked server.modules we need to add the following highlighted line to the file

server.modules = (
        "mod_access",
        "mod_alias",
        "mod_compress",
        "mod_redirect",
        "mod_fastcgi",
       "mod_rewrite", )

And at the bottom of the file we need to add the following text:

fastcgi.server = ( ".php" => ((
                  "bin-path" => "/usr/bin/php-cgi",
                  "socket" => "/tmp/php.socket"
              )))

4. Restart lighttpd service:

# service lighttpd restart

5. Add permission of execution to script xbeeo2 for the user www-data with visudo. The website is host in "/var/www" directory.

www-data ALL=NOPASSWD: /var/www/resources/xbeeo2
