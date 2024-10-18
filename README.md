
# ACQ400_HTTPD_SEC

Secure version of the ACQ400_HTTPD package

## Auth

Auth is forced on

If no auth file is in /mnt/local/sysconfig/auth login will fallback to admin:admin

To create custom login file
```bash
  #create clean auth file
  touch auth

  #Add user and password
  htpasswd auth <username>
```
Save custom auth here /mnt/local/sysconfig/auth

## SSL

SSL is forced on

Instructions to install certificate [here](https://d-tacq.co.uk/pdfs/installing_master_ca.pdf)