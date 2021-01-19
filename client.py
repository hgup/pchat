import socket
import pickle

class Client:

    def __init__(self,username):
        # create client socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = '' # enter the server ip you wanna connect to
        self.port = 1234 # use the same port on which the server is active
        self.addr = (self.host, self.port)

        reply = self.send(username)
        try: # init data here
            self.id = pickle.loads(reply) # unpack data
        except:
            print(reply) # if conn lost


    def send(self,data):
        try: # connect to server addr
            self.socket.send(pickle.dumps(data))
            reply = self.client.recv(2048)
            return reply
        except Exception as err:
            print(err)

    def receive(self):
        try:
            reply = pickle.loads(self.client.recv(2048))
            if reply:
                return reply
        except Exception as err:
            print(err)
