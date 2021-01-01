import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#For UDP Protocols

ip = "0.0.0.0" #This will Listen to all clients trying for Connections
port = 5555

s.bind((ip, port)) #Binds with the ip on port 5555
x = s.recvfrom(1024) #receives message from the client
clientip = x[1][0] #Shows ClientIP
encodedMessage = x[0] #Shows Message In Bytes[DataType]
message = encodedMessage.decode() #Decodes Byte DataType to Str
print(clientip + ": " + message)#Displays the message with ClientIP