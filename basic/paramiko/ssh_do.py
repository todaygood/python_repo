#!/usr/bin/python -tt 

import paramiko


hostname = '10.54.12.29'
port = 22

#username = 'root'
#password = 'novell'

if __name__ == "__main__":
	paramiko.util.log_to_file('paramiko.log')

	s = paramiko.SSHClient()
	s.load_system_host_keys()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#s.load_system_host_keys("/root/.ssh/known_hosts")
	
	s.connect(hostname, port)

	stdin, stdout, stderr = s.exec_command('ifconfig')

	print stdout.read()
	s.close()
	
	
 
