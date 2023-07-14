import socket
import math
import threading
from Hardware import get_data
from HardwareDatabase import database_input
server_port = 6001
hardware_id = str(server_port)
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
welcome_socket.bind(('0.0.0.0',server_port))
welcome_socket.listen(1)

r_val = "!"
s_val = "!"
b_val = "!"

button_status = "!"
def get_button_status():
    global button_status
    while True:
        temp = get_data(hardware_id)
        if temp != "null":
            if temp['elements']['button'] == "on":
                button_status = "1"
            else:
                button_status = "0"

thr = threading.Thread(target = get_button_status)
thr.start()

def send_button():
    global button_status
    i = 0
    while True:
        if i % 10000 == 0:
            connection_s, caddr2 = welcome_socket.accept()
            connection_s.send(button_status.encode())
        i+=1

thr2 = threading.Thread(target = send_button)
thr2.start()

while True:
    connection_socket, caddr = welcome_socket.accept()
    cmsg = connection_socket.recv(1024)
    cmsg = cmsg.decode()

    values = cmsg.split(' ')

    if values[0] == "button":
        if values[2][0] != b_val:
            if values[2][0] == "1":
                button_state = get_data(hardware_id)['elements']['button']
                if button_state == "on":
                    print(database_input(values[0], "off", hardware_id))
                else:
                    print(database_input(values[0], "on", hardware_id))
            b_val = values[2][0]
    elif values[0] == "switch":
        if values[2][0] != s_val:
            print(database_input(values[0], str(values[2])[0], hardware_id))
            s_val = values[2][0]
    elif values[0] == "rotate":
        if values[2][0] != r_val:
            print(database_input(values[0], str(values[2])[0], hardware_id))
            r_val = values[2][0]
