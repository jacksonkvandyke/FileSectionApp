import socket

class socketClass:

    #Initialize socket object
    def __init__(self):
        self.socket = None
        self.port = None
        self.address = None
        self.connectSocket = None
    
    #Create socket object
    def createSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

####This simply creates the socket at the moment but will be fully implemented to make connection between microservices easy to implement.
####This is a work in progress.