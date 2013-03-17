#!/usr/bin/python
import socket, sys, os, threading

class IonicDB:
    def __init__(self):
        self.port = int(sys.argv[1])
        self.cmds = {
                
                "select":self.select,
                "insert":self.insert,
                "remove":self.remove,
            
                }
    def main(self):
        s = socket.socket()
        s.bind(('', self.port))
        s.listen(1)
        while True:
            self.obj, conn = s.accept()
            data = self.obj.recv(1024)
            if not data:
                continue
            try:
                data = eval(data)
            except:
                print 'error data'
                continue
            self.cmd = data[0]
            self.system = data[1]
            self.query = data[2]
            try:
                threading.Thread(target=self.cmds[self.cmd]).start()
            except Exception, error:
                print error
                pass
    def select(self):
        if not os.path.exists(self.system+".ion"):
            with open(self.system+".ion", 'w') as file:
                pass
            self.obj.close()
        else:
            with open(self.system+".ion", 'rb') as file:
                for x in file.readlines():
                    if self.query.strip("{").strip("}") in x:
                        self.obj.send(x)
                self.obj.close()
    def insert(self):
        if not os.path.exists(self.system+".ion"):
            with open(self.system+".ion", 'w') as file:
                pass
        with open(self.system+".ion", 'ab') as file:
            file.write(self.query+"\n")
        self.obj.close()
    def remove(self):
        if not os.path.exists(self.system+".ion"):
            pass
        else:
            with open(self.system+".ion", 'rb') as file:
                stuff = file.read().split("\n")
                out = []
                query = str(self.query).strip("{").strip("}")
                for x in stuff:
                    if x == '' or query in x:
                        continue
                    else:
                        out.append(x)
                with open(self.system+".ion", 'wb') as outs:
                    for x in out:
                        outs.write(x+"\n")

if __name__ == "__main__":  
    if len(sys.argv) < 2:
        print 'Usage: ionic-server <port>'
        exit()
    IonicDB().main()
