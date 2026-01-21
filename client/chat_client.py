import socket

HOST = "127.0.0.1"
PORT = int(input("Enter server port: "))

while True:
    msg = input("Message: ")
    if msg.lower() == "exit":
        break

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(msg.encode())
    s.close()
