import client
import _thread

class app:

    def __init__(self):
        self.username = self.getUsername()
        self.net = client.Client(self.username)
        _thread.start_new_thread(self.session,())
        self.active()

    def getUsername(self):
        print('''
         ____            _           _
         |  _ \       ___| |__   __ _| |_
         | |_) |____ / __| '_ \ / _` | __|
         |  __/_____| (__| | | | (_| | |_
         |_|         \___|_| |_|\__,_|\__|

         ENTER USERNAME:
        ''')
        a = ''
        while not a:
            a = input('\t ->')
        return a
    
    def active(self):
        while True:
            x = f'[{self.username}]: '+input(f'[{self.username}]')
            self.net.send(x)

    def session(self):
        while True:
            R = self.net.receive()
            if R is not None:
                print('lol',R)

if __name__ == "__main__":
    app()
