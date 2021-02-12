# Hermes
A a socket server built into a python generator object

## hermes.listen(port, [listen_num, size_limit, log_function])
listens on the port, yields the data recieved and the connection object
```
for data, conn in hermes.listen(8080, log_function=print):
    # do something cool with the data
    print(data)
    
    conn.send("Okay!".encode())
```

## hermes.send(message, port, [log_function])
simple script to send a message, not super important, any old socket can work with hermes!