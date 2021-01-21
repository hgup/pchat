import select
import sys
import pickle
import socket
import settings
import time
colors = {
    'red': "\u001b[31m",
    'green': "\u001b[32m",
    'yellow': "\u001b[33m",
    'magenta': "\u001b[35m",
    'cyan': "\u001b[36m",
    'white': "\u001b[37m",
}
class app:

    def __init__(self):
        self.logo()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(1)
        if len(sys.argv) < 2:
            self.username = self.getUsername()
        else:
            self.username = sys.argv[1]
        if len(sys.argv) < 3:
            self.host = input('enter HOST name:')
            self.port = int(input('enter port:'))
        else:
            parse = sys.argv[2].split(':')
            self.host = parse[0]
            self.port = int(parse[1])
        self.port = self.port # use the same port on which the server is active
        self.addr = (self.host, self.port)
        self.connect(self.username)
        self.session()

    def connect(self,uname):
        # connect self to self.addr
        self.socket.connect(self.addr)
        self.color = pickle.loads(self.socket.recv(2048))
        self.socket.send(pickle.dumps(uname))

    def logo(self):
        print(colors['yellow']+'''
          ____            _           _
         |  _ \       ___| |__   __ _| |_
         | |_) |____ / __| '_ \ / _` | __|
         |  __/_____| (__| | | | (_| | |_
         |_|         \___|_| |_|\__,_|\__|

        ''')
    def getUsername(self):
        print('\tENTER USERNAME:\n\n')
        a = ''
        while not a:
            print('\033[A',end = '')
            a = input('\t ->')
        return a
    
    def session(self):
        run = True
        while run:
            input_streams = [sys.stdin, self.socket]
            readable, writable, exceptional = select.select(input_streams,[],[])

            for inputs in readable:
                if inputs == self.socket:
                    msg = pickle.loads(self.socket.recv(2048))
                    print(msg)
                elif inputs == sys.stdin:
                    messege =  sys.stdin.readline().strip()
                    if messege == '/exit':
                        run = False
                    sys.stdout.write('\033[A')
                    sys.stdout.write(colors[self.color]+'[You]: '+colors['white']+str(messege)+'\n')
                    sys.stdout.flush()
                    self.socket.send(pickle.dumps(messege))

if __name__ == "__main__":
    app()
