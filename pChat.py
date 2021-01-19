import client
class app:

    def __init__(self):
        self.username = self.getUsername()
        self.net = client.Client(self.username)

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

if __name__ == "__main__":
    app()
