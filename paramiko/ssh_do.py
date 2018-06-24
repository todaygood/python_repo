#!/usr/bin/python -tt 

import paramiko


hostname = '192.168.5.51'
port = 22

username = 'root'
password = 'novell'

if __name__ == "__main__":
	paramiko.util.log_to_file('paramiko.log')

	s = paramiko.SSHClient()
	s.load_system_host_keys()
	
	s.connect(hostname, port, username, password)

	stdin, stdout, stderr = s.exec_command('ifconfig')

	print stdout.read()
	s.close()
	
	
 
