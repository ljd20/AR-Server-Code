import socket
import math
from Hardware import get_data
from pprint import pprint
print("We're in tcp server...");
#select a server port
server_port = 7001
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
    temp = server_port - 1000
    sends = get_data(str(temp))
    if sends:
        print("Got data:")
        pprint(sends)
        #if hasattr(sends, 'elements'):
         #   item = sends['elements']
          #  sending = (item['button'])
#    item = sends['elements']
#    switch = item['switch']
#    rotate = item['rotate']
#    final = f"{button}"
#    print(sending)
    connection_socket.send(str(sends['elements']).encode())



