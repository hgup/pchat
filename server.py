import socket
import _thread
import pickle

class Server:

    def __init__(self, peers):
        self.server = ''
        self.port = 6666
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

    def acceptRequest(self):
        self.connections = []
        c = 0
        while True:
            c += 1
            print(f'[{c}] Waiting')
            # accept client request
            conn,addr = self.socket.accept()
            self.connections.append((conn,addr))
            # start a new client thread with conn obtained
            _thread.start_new_thread(self.clientThread,(conn,))

    def getId(self):
        # make your own id generation system, you may use conn addr and passwords
        return 1

    def clientThread(conn):
        #initial send
        _id = self.getId()
        conn.send(pickle.loads(_id))
        # mainloop
        self.mainloop(conn)
        # close connection
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

    def mainloop(conn):
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                self.chats = data
                conn.send(pickle.dumps(reply))
                if self.chats == data:
                    self.chats = ''
            except Exception as err:
                # if connection lost
                print(err)

if __name__ == "__main__":
    Server(int(input('No. of connections?: ')))
