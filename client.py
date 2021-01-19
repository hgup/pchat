import socket
import pickle

class Client:

    def __init__(self,username):
        # create client socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = '' # enter the server ip you wanna connect to
        self.port = 6666 # use the same port on which the server is active
        self.addr = (self.host, self.port)

        reply = self.connect()
        try: # init data here
            self.id = pickle.loads(reply) # unpack data
        except:
            print(reply) # if conn lost

    def connect(self):
        # connect self to self.addr
        self.socket.connect(self.addr)
        return self.socket.recv(32).decode() #id

    def send(self,data):
        try: # connect to server addr
            self.socket.send(pickle.dumps(data))
            reply = self.socket.recv(2048)
            return reply
        except Exception as err:
            print(err,'this')

    def receive(self):
        try:
            reply = pickle.loads(self.socket.recv(2048))
            print(type(reply))
            if  '-~=' in reply:
                return reply
        except Exception as err:
            pass

if __name__ == "__main__":
    Client('hursh')
