import socket
import pyperclip                              #python's clipboard module

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))

while 1:
    print("TCPServer Waiting for client on port 5000\n")
    server_socket.listen(5)
    client_socket, address = server_socket.accept()
    print("I got a connection from "+ address[0]+"\n")
    data = pyperclip.paste()
    client_socket.send(bytes(data, 'UTF-8'))
    print("Sent Clipboard data to "+address[0]+" :- \n"+ data+"\n")
    data = client_socket.recv(1024)
    pyperclip.copy(str(data,'utf-8'))
    print("Clipboard set to :- \n" + str(data,'utf-8') + "\n\n\n")
    client_socket.close()
