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
        self.service = subprocess.Popen(microPath)

        # Create socket to connect to microservice
        self.connection = socket.socket()
        try:
            self.connection.connect((socket.gethostname(), 7245))
            print("Socket successfully connected")
        except:
            print("Socket connection unsuccessful")

    def SaveFile(self, fileDirectory):
        # Save file to database
        saveString = "save," + fileDirectory + ",save"
        self.connection.send(saveString.encode())
        self.connection.close()

    def RetrieveFile(self, fileDirectory):
        # Save file to database
        retrieveString = "," + fileDirectory + ",retrieve"
        self.connection.send(retrieveString.encode())
        self.connection.close()
        