import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    clientsocket, address=s.accept()
    print(f"Connection from{address} has been been established!")
    clientsocket.send(bytes("Welcome","utf-8"))
    clientsocket.close()