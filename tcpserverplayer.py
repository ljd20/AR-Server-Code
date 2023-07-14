import socket
import math
from Player import get_data
from PlayerDatabase import database_input
from pprint import pprint
print("We're in tcp server...");
#select a server port
server_port = 7000
#create a welcoming socket
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#bind the server to the localhost at port server_port
welcome_socket.bind(('0.0.0.0',server_port))
welcome_socket.listen(1)
#ready message
print('Server running on port ', server_port)
#Now the main server loop


while True:
    connection_socket, caddr = welcome_socket.accept()
     #notice recv and send instead of recvto and sendto
    cmsg = connection_socket.recv(1024)
    cmsg = cmsg.decode()

    values = cmsg.split('/')
    nscoord = str(values[0])
    ewcoord = str(values[1])
    username = str(values[2])

    lists = database_input(nscoord, ewcoord, username)

    connection_socket.send(lists.encode())





# To get all the data from database
# form a transmissible string to send to client
# split string on client side
