#!/usr/bin/python

import socket, sys

class IonicDBClient:
    def __init__(self):
        self.port = int(sys.argv[2])
        self.ip = sys.argv[1]
        self.cmds = {
                "select":self.select,
                "insert":self.insert,
                "remove":self.remove,

                }
    def main_loop(self):
        while True:
            try:
                cmd = raw_input("IonicDB> ").split()
                if cmd[0] == "exit":
                    break
                try:
                    self.cmd = cmd[0]
                    self.system = cmd[1]
                    self.query = cmd[1:]
                    self.query.remove(self.system)
                    self.query = ' '.join(self.query)
                    self.cmds[self.cmd]()
                except Exception, error:
                    print error
                    print "Invalid Syntax"
            except:
                continue
    def select(self):
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        query = """("{0}", "{1}", "{2}")""".format(self.cmd, self.system, self.query)
        sock.send(query)
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print data
        sock.close()
    def insert(self):
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        query = """("{0}", "{1}", "{2}")""".format(self.cmd, self.system, self.query)
        sock.send(query)
        sock.close()
    def remove(self):
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        query = """("{0}", "{1}", "{2}")""".format(self.cmd, self.system, self.query)
        sock.send(query)
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Usage: ionic <host> <port>"
        exit()
    IonicDBClient().main_loop()

