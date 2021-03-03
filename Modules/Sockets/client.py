import socket

#CONSTANTS
HEADER = 64
PORT = 5050
SERVER = "192.168.29.87"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    msg_len_encoded = str(len(msg)).encode(FORMAT)
    msg_length = msg_len_encoded + b' '*(HEADER - len(msg_len_encoded))
    print(msg_length)
    client.send(msg_length)
    
    msg_encoded = msg.encode(FORMAT)
    print(msg_encoded)
    client.send(msg_encoded)
    print(client.recv(2048).decode(FORMAT))
    

    
    