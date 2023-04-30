import MySQLdb as mbd


class db():
    def createConnection(self):
        try:
            conn = mbd.connect('localhost', 'root', '', 'hospita_system')
            return conn
        except mbd.Error:
            print("error connexion")
