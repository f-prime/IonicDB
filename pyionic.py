import socket

class pyionic:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)
    def insert(self, system, query):
        s = socket.socket()
        s.connect((self.ip, self.port))
        query = """("{0}","{1}","{2}")""".format("insert", system, str(query))
        s.send(query)
        s.close()
    def select(self, system, query):
        s = socket.socket()
        s.connect((self.ip, self.port))
        query = """("{0}","{1}","{2}")""".format("select", system, str(query))
        s.send(query)
        data = []
        while True:
            d = s.recv(1024)
            if not d:
                break
            data.append(d)
        s.close()
        b = []
        d = ' '.join(data).split("\n")
        for x in d:
            if x == '':
                continue
            b.append(eval(x))
        return b
    def remove(self, system, query):
        s = socket.socket()
        s.connect((self.ip, self.port))
        query = """("{0}","{1}","{2}")""".format("remove", system, str(query))
        s.send(query)
        s.close()
    def update(self, system, query):
        s = socket.socket()
        s.connect((self.ip, self.port))
        query = """("{0}","{1}","{2}")""".format("update", system, str(query))
        s.send(query)
        s.close()
