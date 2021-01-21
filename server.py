import socket
import _thread
import pickle
import settings
import sys
import random

colors = {
    'red': "\u001b[31m",
    'green': "\u001b[32m",
    'yellow': "\u001b[33m",
    'magenta': "\u001b[35m",
    'cyan': "\u001b[36m",
    'white': "\u001b[37m",
}

class Server:

    def __init__(self, peers):
        self.colorKeys = list(colors.keys())[:-1]
        self.server = ''
        self.port = int(sys.argv[2])
        print(colors['cyan']+'server open at localhost:'+str(self.port))
        self.peers = peers
        self.chats = ''

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = socket.gethostbyname(self.server)
        self.bind()

        self.socket.listen(self.peers)
        self.acceptRequest()

    def bind(self):
        try:
            self.socket.bind((self.server, self.port))
        except socket.error as err:
            print(str(err))

    def getColor(self):
        col = random.choice(self.colorKeys)
        self.colorKeys.remove(col)
        if not self.colorKeys:
            self.colorKeys = list(colors.keys())[:-1]
        return col

    def acceptRequest(self):
        try:
            self.connections = {}
            c = 0
            while True:
                c += 1
                print(colors['yellow']+f'[{c}] Waiting'+colors['white'])
                # accept client request
                conn,addr = self.socket.accept()
                mycolor = self.getColor()
                conn.send(pickle.dumps(mycolor))
                uname = pickle.loads(conn.recv(2048))
                self.connections[conn] = [addr,True,uname]
                self.broadcast(colors['green']+f'{addr} {colors["white"]}joined the chat as {colors[mycolor]}[{uname}]'+colors['white'],None)
                # start a new client thread with conn obtained
                _thread.start_new_thread(self.clientThread,(conn,mycolor))
        except:
            self.closeClient(self.socket)


    def clientThread(self,conn,mycolor):
        # mainloop
        user = self.connections[conn][2]
        self.mainloop(conn,mycolor)
        # close connection
        self.broadcast(colors['red']+f'{user} left the chat'+colors['white'],None)

    def closeClient(conn):
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

    def mainloop(self,conn,mycolor):
        while self.connections[conn][1]:
            try:
                messege = pickle.loads(conn.recv(2048))
                if messege:
                    messegeSent = colors[mycolor]+f'[{self.connections[conn][2]}]:'+colors['white'] + messege
                    self.broadcast(messegeSent,conn)
                else:
                    break
            except Exception as err:
                print(err)
                break

    def broadcast(self, messege, sender):
        print(messege)
        for conn in self.connections:
                try:
                    if conn != sender:
                        conn.send(pickle.dumps(messege))
                except Exception as err:
                    self.connections[conn][1] = False
                    continue

if __name__ == "__main__":
        serv = Server(int(sys.argv[1]))
