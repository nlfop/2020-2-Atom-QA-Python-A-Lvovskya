

import pytest
from Mock.Mock_server import MockServer
import socket

HOST = '127.0.0.1'
PORT = 9000


@pytest.fixture(scope='function')
def app():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    yield s
    s.close()


@pytest.fixture(scope='session')
def mock_server():
    server = MockServer(HOST,PORT)
    server.start()
    yield server
    server.stop()


def test_connect_error():#Y1
    with pytest.raises(ConnectionRefusedError):
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((HOST, PORT))

def test_put (mock_server,app):#Y3
    DATA_PUT = "user: admin"
    DATA_LEN2 = str(len(DATA_PUT))
    app.send(("PUT /search.php HTTP/1.1\r\nHost: " + HOST + "\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " + DATA_LEN2 + "\r\n\r\n" + DATA_PUT).encode())


    responce = []

    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code == 201


def test_users(mock_server,app):#I1
    request = f'GET {"/search.php"} HTTP/1.1\r\nHost:{HOST}\r\n\r\n'
    app.send(request.encode())
    responce = []

    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code is 200


@pytest.mark.skip('no need')
def test_time_error():#Y2
    with pytest.raises(TimeoutError):
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("192.168.1.157", 5555))


def test_unsupported_method(mock_server,app):#I2
    request = f'GETfds {"/search.php"} HTTP/1.1\r\nHost:{HOST}\r\n\r\n'
    app.send(request.encode())
    responce = []

    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code == 501


def test_500(mock_server,app):#Y3
    request = f'PUT {"/"} HTTP/1.1\r\nHost:{HOST}\r\n\r\n'
    app.send(request.encode())
    responce = []

    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code == 500


def test_authorization(mock_server,app):#Y4.1
    DATA_POST = "'user':admin&'pass':123"
    DATA_LEN = str(len(DATA_POST))
    app.send(("POST /login.php HTTP/1.1\r\nHost: " + HOST + "\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " + DATA_LEN + "\r\n\r\n" + DATA_POST).encode())
    responce = []
    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code is 200


def test_authorization_error1(mock_server,app):#Y4.2
    DATA_POST = "'user':admin&'pass':12gde3"
    DATA_LEN = str(len(DATA_POST))
    app.send(("POST /login.php HTTP/1.1\r\nHost: " + HOST + "\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " + DATA_LEN + "\r\n\r\n" + DATA_POST).encode())
    responce = []
    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code == 404


def test_authorization_error2(mock_server,app):#Y4.3
    DATA_POST = "'user':admin&'pass':12gde3"
    DATA_LEN = str(len(DATA_POST))
    app.send(("POST /search.php HTTP/1.1\r\nHost: " + HOST + "\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " + DATA_LEN + "\r\n\r\n" + DATA_POST).encode())
    responce = []
    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code == 405


def test_connection_error(mock_server,app):
    request = f'GET {"/serch.pp"} HTTP/1.1\r\nHost:{HOST}\r\n\r\n'
    app.send(request.encode())
    responce = []

    while True:
        data = app.recv(4096)
        if data:
            responce.append(data.decode())
        else:
            break
    data = ''.join(responce).splitlines()
    code = int(data[0][9:12])
    assert code == 404


def test_net_connection():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipaddr = socket.gethostbyname('devwerks.net')
    s.connect((ipaddr, 80))

    data = "username=test&pass=blah\n\n"
    header = ("""
    POST /index.php HTTP/1.1
    Host: devwerks.net
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Referer: http://google.com
    Cookie: PHPSESSID=blub
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    """)

    contentLength = "Content-Length: " + str(len(data)) + "\n\n"
    request = header + contentLength + data
    s.send(request.encode())
    response = s.recv(4096).decode()
    s.close()
    data = ''.join(response).splitlines()
    code = int(data[0][9:12])
    assert code == 400