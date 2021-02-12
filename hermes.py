"""
The following is a proof of concept

The concept is a python Socket server built into a generator object
This idea came to me in a dream

I decided to yield the data recieved and also the connection,
 in case the user wants to send a response.

log_function is a function, you could pass it print or some other logging function
"""
import socket

def off(*args, **kwargs): pass

def listen(port, listen_num=1, size_limit=1024, log_function=off):
    host = socket.gethostname()
    sock = socket.socket()

    sock.bind((host, port))
    log_function("socket bound at ({}, {})".format(host, port))

    sock.listen(listen_num)

    conn, addr = sock.accept()
    log_function("connection recieved at {}".format(addr))

    while True:
        data = conn.recv(1024).decode()
        log_function("recieved data : {}".format(data))
        if not data:
            break

        yield data, conn

    conn.close()
    log_function("connection at {} closed".format(data))

def send(message, port, log_function=off):
    host = socket.gethostname()
    sock = socket.socket()

    sock.connect((host, port))
    log_function("socket bound at ({}, {})".format(host, port))

    sock.send(message.encode())
    log_function("message sent: {}".format(message))
    
    sock.close()
    log_function("connection closed")

