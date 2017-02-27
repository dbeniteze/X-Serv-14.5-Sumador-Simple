import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostbyname(socket.gethostname()), 1235))
mySocket.listen(2)
wait_first = True

try:
    while True:
        print('Waiting for connections')
        print socket.gethostbyname(socket.gethostname())
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        url = recvSocket.recv(1024)
        sumando = url.split("/")[1].split()[0]
        if wait_first:
            sumando_1 = int(sumando)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" + str(sumando_1) +
                            "</p>" + " esperando segundo sumando" +
                            "</body></html>" + "\r\n")
            wait_first = False
        else:
            suma = sumando_1 + int(sumando)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" + str(sumando_1) +
                            "+" + str(sumando) + "\r\n" +
                            "</p>" + "La suma es : " + str(suma) +
                            "</body></html>" + "\r\n")
            wait_first = True
            recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
except ValueError:
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body></p> Error uso: " +
                    "Introduzca un numero valido " +
                    "</body></html>" + "\r\n")
recvSocket.close()
