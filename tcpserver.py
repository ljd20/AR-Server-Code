import socket
import boto3
from Hardware import get_data
import threading
from datetime import datetime

#select a server port
server_port = 5000
#create a welcoming socket
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the server to the localhost at port server_port
welcome_socket.bind(('0.0.0.0',server_port))
welcome_socket.listen(1)
#Now the main server loop

global_message = "default message"


def send_msg(message):
    connection_socket.send(message.encode())

def change_global_message():
    global global_message
    while True:
        global_message = input("Message to send: ")

#thr = threading.Thread(target=change_global_message)
#thr.start()

while(1):
    connection_socket, caddr = welcome_socket.accept()
    msg = connection_socket.recv(1024)
    print(msg.decode())
    #data = get_data('12000')['elements']['button']
    send_msg(current_time)
