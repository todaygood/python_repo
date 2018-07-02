#!/usr/bin/python -tt 

import paramiko


def remote_ssh_exec(hostname,cmd):
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    s.connect(hostname)
    
    stdin, stdout, stderr = s.exec_command(cmd)
    
    s.close()
    return stdin,stdout,stderr
	
	
 
if __name__ == "__main__":
    hostname = '10.54.12.29'
    remote_ssh_exec(hostname,"ifconfig")

