import socket
import json

def replicate_message(message, nodes, self_port):
    for node in nodes:
        if node["port"] != self_port:
            try:
                s = socket.socket()
                s.connect((node["host"], node["port"]))
                s.send(message.encode())
                s.close()
            except:
                pass
