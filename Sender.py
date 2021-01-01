import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#Connecting Via UDP Protocol
ip = str(input("Enter Server IP: "))#Put in server IP
port = int(input("Enter Server Port: "))#Put in Server PORT

#This funcition Connects client to the server for remote code execution
def command(ip, port):
    username = input("Enter Your Username: ")
    message = username.encode()
    s.sendto(message, (ip, port))

#Port 4444 is for remote code execution
if port == 4444:
    command(ip, port)
#Port 5555 is for messaging
elif port ==5555:
    message = input("Enter Your Message: ")
    message = message.encode() #This converts string to bytes
    s.sendto(message , (ip, port)) #This sends the message with clientip and clientport to the server
else:
    print("Wrong port number")