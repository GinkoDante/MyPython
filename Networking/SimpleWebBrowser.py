import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to web server at port 80
mysock.connect(('www.py4inf.com', 80))
# Send command to get text file
request = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
mysock.send(request.encode())

while True:
    data = mysock.recv(512).decode()
    if ( len(data) < 1 ) :
        break
    print(data)

mysock.close()