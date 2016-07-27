import json
import subprocess
import re
import socket

filtered = ['192.168', '10', '255.255.255.255']

logfile = open('/var/log/access.log', 'a')
f = subprocess.Popen(['tail','-F',"/var/log/ulog/syslogemu.log"],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
    usersFile = open("/home/Administrator/CaptivePortal/users", "r")
    users = json.load(usersFile) 

    line = f.stdout.readline().decode("utf-8")
    l = json.loads(str(line))

    src_ip = l['src_ip']
    destination = l['dest_ip'].strip()
    source = l['mac.saddr.str'].strip()

    try:
        if  destination.startswith(tuple(filtered)):
            continue

        source = users[source]
        destination = socket.gethostbyaddr(destination)[0]
    except:
        None
    
    logfile.write('%s %s\n' % (source, destination))
    logfile.flush()
