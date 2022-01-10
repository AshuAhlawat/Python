import socket
import threading

#CONSTANTS
HEADER = 64 #bytes
PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "!Logout"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

pos=["480,100","480,100"]

#function which will run concurrently
def handle_client(conn, player):
    conn.send(pos[player].encode())
    reply = ""
    
    connected = True
    while connected:
        #waiting till data is recieved from client
        try:
            msg = conn.recv(256).decode()
            pos[player]=msg
            if msg!="":    
                if msg == DISCONNECT_MSG:
                    connected = False
                    print(f"Player {player+ 1} DISCONNECTED")
                    player -= 1
                else:
                    if player==1:
                        reply = pos[0]
                    if player==0:
                        reply = pos[1]
            if not msg:
                print(f"Player {player + 1} DISCONNECTED")
                player -= 1
                break
            conn.send(reply.encode())
        except:
            break
    conn.close()


print(f"\nSERVER started...")
server.listen(2)

player = 0
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, player))
    thread.start()
    player += 1
    print(f"CONNECTIONS : {threading.active_count() - 1}")


