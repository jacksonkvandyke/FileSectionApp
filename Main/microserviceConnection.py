#Import  microservice requirements
import subprocess
import os
import sys
import socket

class MicroserviceConnection:

    def __init__(self):
        self.service = None
        self.connection = None

    def ConnectService(self):
        # Get file path
        appPath = os.getcwd()
        microPath = "python " + appPath + "\\save-retrieve-Program-main\\save-retrieve-Program-main\\server.py"
        print(microPath)
        self.service = subprocess.Popen(microPath)

        # Create socket to connect to microservice
        self.connection = socket.socket()
        try:
            self.connection.connect((socket.gethostname(), 7245))
            num1 = "retrieve/TifaandCloud.png,TifaandCloud.png,retrieve"
            self.connection.send(num1.encode())
            print("Socket successfully connected")
        except:
            print("Socket connection unsuccessful")
        