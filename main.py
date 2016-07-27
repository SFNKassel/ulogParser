import json
import subprocess
import re
import socket

filtered = ['192.168', '10']

f = subprocess.Popen(['tail','-F',"/var/log/ulog/syslogemu.log"],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
    usersFile = open("/home/Administrator/CaptivePortal/users", "r")
    users = json.load(usersFile) 

    line = f.stdout.readline().decode("utf-8")
    l = json.loads(str(line))

    src_ip = l['src_ip']
    dest_ip = l['dest_ip']
    mac = l['mac.saddr.str']

    try:
        if not dest_ip.startswith(tuple(filtered)):
            dest_ip = socket.gethostbyaddr(dest_ip)[0]

        mac = users[mac]
    except:
        None
    
    print(mac, end=' ')
    	
    print(dest_ip)
