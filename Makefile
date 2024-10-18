# Makefile for httpd
#
DC=$(shell date +%y%m%d%H%M)
SEQ=20
PN=httpd_sec

package:
	rm -Rf opkg/usr/local/*
	mkdir -p opkg/usr/local/init opkg/usr/local/bin opkg/usr/local/var/www opkg/etc
	cp -av init/* opkg/usr/local/init
	cp -av bin/* opkg/usr/local/bin
	cp -av www/* opkg/usr/local/var/www
	cp -av etc/* opkg/etc
	mkdir -p release
	tar czf release/$(SEQ)-$(PN)-$(DC).tgz -C opkg .
	@echo Created release/$(SEQ)-$(PN)-$(DC).tgz
	rm -f ../PACKAGES.OPT/$(SEQ)-$(PN)*
	cp release/$(SEQ)-$(PN)-$(DC).tgz ../PACKAGES.OPT/


