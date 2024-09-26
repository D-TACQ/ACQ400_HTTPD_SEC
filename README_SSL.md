# HTTPD now supports ssl
## To enable SSL
add these lines to /mnt/local/sysconfig/acq400.sh and uncomment as appropriate
```bash
# SSL: hostname.crt, hostname.key should reside in /mnt/local/sysconfig/ssl
# enable SSL (https://) with embedded certificate alongside http://
#SSL_MODE=ON
# enable SSL ONLY. Best to test with "ON" first
#SSL_MODE=FORCE
# set location of CA. Default shown below:
#SSL_CA_POPUP_LINK=https://www.d-tacq.com/acq400_ssl.shtml
```

## to Add password authentication:
add these lines to /mnt/local/sysconfig/acq400.sh and uncomment as appropriate
```bash
# password protection for web site. i
# password is held /mnt/local/sysconfig/auth
#SSL_MODE=FORCE
#WEB_AUTH=ON
```

# Users may prefer to set their own certificate authority.

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
	-keyout ./mnt/local/nginx/nginx-selfsigned.key \
	-out ./mnt/local/nginx/nginx-selfsigned.crt

# To create a password:
Using a host PC with htpasswd(1) command
https://linux.die.net/man/1/htpasswd
```
> touch auth
> htpasswd auth <username>
copy file auth to uut at /mnt/local/sysconfig/auth
```




