import socket
import threading


#CONSTANTS
HEADER = 64 #bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!Logout"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#function which will run concurrently
def handle_client(conn, addr):
    print(f"{addr} CONNECTED")
    
    connected = True
    while connected:
        #waiting till data is recieved from client
        msg_length_encoded = conn.recv(HEADER)
        msg_length = msg_length_encoded.decode(FORMAT)
        
        if msg_length!="":
            msg_length = int(msg_length)
            
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MSG:
                connected = False
                print(f"{addr} DISCONNECTED")
            else:
                print(f"{addr} : {msg}")
                conn.send("received..".encode(FORMAT))
            
            
    
    conn.close()

def start():
    print(f"\nSERVER[{ADDR}] started...")
    server.listen(2)
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"CONNECTIONS : {threading.active_count() - 1}")



start()
