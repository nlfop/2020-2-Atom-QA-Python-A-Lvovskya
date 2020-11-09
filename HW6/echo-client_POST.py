import json
import socket

HOST = '127.0.0.1'
PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

DATA_POST = "password"
DATA_LEN = str(len(DATA_POST))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(("POST /search.php HTTP/1.1\r\nHost: "+ HOST +"\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: "+ DATA_LEN +"\r\n\r\n" + DATA_POST).encode())

responce = []

while True:
    data = s.recv(4096)
    if data:
        responce.append(data.decode())
    else:
        break

print(json.dumps(responce))
s.close()
