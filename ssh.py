#!/usr/bin/python
# -*- coding: utf-8 -*-
# ssh to a host
import paramiko

hostname = '192.168.122.4'
port = 22
username = 'root'
password = 'oo11PS@123'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('iconfig')
    print stdout.read()
    print stderr.read()
#    print stdin.read()
    s.close()
raw_input("")
