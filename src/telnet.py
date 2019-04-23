# Adapted from https://grocid.net/2012/06/14/a-very-simple-server-telnet-example/

import socket
import threading
import brain
import markovify

model = None
with open("model.json", "r") as infile:
    model = markovify.NewlineText.from_json(infile.read())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8192))
s.listen(15)

lock = threading.Lock()

welcome_message = """
 WELCOME TO THE ROBOT MIND OF @DRIL
      
   |=-=-=-=-=-=-=-=-=-=-=-=-=-=|
   | forget the world Wide Web |
   |  telnet to @dril insted!  |
   |=-=-=-=-=-=-=-=-=-=-=-=-=-=|  

 BUILT WITH PYTHON AND MANY good TOOLS
            
            BAD WORDS NOT MY
            fault

the internet is tubes, welcome to ours

markov is fucked, there May be similarities
to ""real"" @dril content 

(enter your prompt then press Enter)
((or just press Enter for a suprise))

=============== BEGIN ===============

"""


class daemon(threading.Thread):
    def __init__(self, tupledat):
        socket, address = tupledat
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address

    def run(self):
        self.socket.send(bytes(welcome_message, "utf8"))
        try:
            while True:
                data = self.socket.recv(1024)
                prompt = str(data.decode("utf-8")).replace("\r",
                                                           "").replace("\n", "").strip()
                # print("'%s'" % prompt)
                response = brain.generate_sentence(model, start=prompt)
                self.socket.send(bytes(response + "\n\n", "utf8"))
        except Exception as e:
            print(e)
        self.socket.close()


while True:
    daemon(s.accept()).start()
