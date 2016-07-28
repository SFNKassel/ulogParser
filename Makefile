
depend:

install: depend
	cp -TRf src /usr/local/bin/logparse
	chmod 755 /usr/local/bin/logparse/main.py
	install -o root -g root -m 755 50_logging.sh /etc/security/packetfilter.d/
	install -o root -g root ulogd.conf /etc/
	install -o root -g root -m 755 logparse /etc/init.d/ 		
	update-rc.d logparse defaults
