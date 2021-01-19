import socket
import pickle

class Client:

    def __init__(self):
        # create client socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = '' # enter the server ip you wanna connect to
        self.port = 1234 # use the same port on which the server is active
        self.addr = (self.host, self.port)

        reply = self.connect()
        try: # init data here
            self.id = pickle.loads(reply) # unpack data
        except:
            print(reply) # if conn lost


    def connect(self):
        try: # connect to server addr
            self.socket.send(data)
            reply = self.client.recv(2048)
            return reply
        except Exception as err:
            print(err)
