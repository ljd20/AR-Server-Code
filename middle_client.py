import socket
print("We're in tcp client...");
#the server name and port client wishes to access
server_name = '13.40.71.142'
#'52.205.252.164'
server_port = 7000
#create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Set up a TCP connection with the server
#connection_socket will be assigned to this client on the server side
client_socket.connect((server_name, server_port))

msg = client_socket.recv(1024)
msg = msg.decode()
#values = msg.split('/')
print(msg)


'''
for shame in trying:
    print("username: " + str(values[0]))
    print("North/South Coordinates: " + str(values[1]))
    print("East/West Coordinates: " + str(values[2]))
'''

client_socket.close()

