#!/usr/bin/env python
from flask import Flask
from json import dumps
import shlex, subprocess
app = Flask(__name__)

@app.route('/')
def grep (target, s):
    print(targret.split("\n"))
    for line in target.split("\n"):
        pos = line.find(s)
        if pos != -1:
            return line[pos:]

def ip():
    cmd = ''' ip addr show dev ethO '''
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    ipaddr = ''
    if output:
        s = grep(output, 'inet ')
        pos = s.find('/')
        ippadr = s[5:pos]
    return ipaddr


def hostname():
    cmd = ''' hostname '''
    args = shlex.split(cmd)
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output.strip()
        

def main():
    host_stats = {}

    host_stats['ip'] = ip()
    host_stats['hostname'] = hostname()
    print(dumps(host_stats))
if __name__== '__main__':
    main()