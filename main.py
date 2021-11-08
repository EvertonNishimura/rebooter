#!/usr/bin/env python3
from datetime import datetime
import os
import time
import paramiko

def sshReboot():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    server = '127.0.0.1'
    ssh.connect(server, username='boschrexroth', password='boschrexroth')
    stdin, stdout, stderr = ssh.exec_command('sudo reboot')

def my_func():
    while True:
        ref_time = "00:00:00"
        now = datetime.now().time()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)

        try:
            if current_time == ref_time:
                # TODO: change to "sudo reboot now"
                print("rebooting")
                sshReboot()


        except Exception as err:
            print(err)
        time.sleep(1)


if __name__ == "__main__":
    my_func()



