import socket
import json
from leader_election import elect_leader
from replication import replicate_message

with open("config/nodes.json") as f:
    NODES = json.load(f)["nodes"]

HOST = "127.0.0.1"
PORT = int(input("Enter node port: "))

leader = elect_leader(NODES)
print("Leader Node:", leader)

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print(f"Node running on port {PORT}")

while True:
    conn, addr = server.accept()
    message = conn.recv(1024).decode()
    print("Received:", message)

    if PORT == leader["port"]:
        replicate_message(message, NODES, PORT)

    conn.close()
