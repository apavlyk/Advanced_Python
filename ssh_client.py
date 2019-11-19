#!/usr/bin/python

import paramiko

class SshClient(object):

    def __init__(self, ip, user, password):
        self.ip = ip
        ssh_client = ssh.connect(ip)

    def call(self, cmd):
        cmd = cmd.strip()
        return ssh_client.call(cmd)



ssh_client = SshClient()

if __name__ == '__main__':
    pass
