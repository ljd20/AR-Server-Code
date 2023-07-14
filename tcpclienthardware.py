import socket
print("We're in tcp client...");
#the server name and port client wishes to access
server_name = 'ec2-54-89-71-162.compute-1.amazonaws.com'
#'52.205.252.164'
server_port = 13000
#create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Set up a TCP connection with the server
#connection_socket will be assigned to this client on the server side
client_socket.connect((server_name, server_port))

cmsg = client_socket.recv()

#send the message to the TCP server
client_socket.send(cmsg.encode())

#return values from the server
msg = client_socket.recv(1024) 
msg = msg.decode()
#values = msg.split('')
#print(msg)
print ("Inputted: " + msg)
#print ("Switch: " + str(values[1]))
#print ("Rotated: " + str(values[2]))
client_socket.close() 
