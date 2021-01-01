import socket
import os

while True:
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#For UDP Protocols
  ip = "0.0.0.0" # Listens to all IPs trying to connect
  port = 4444
  s.bind((ip, port)) #Binds with ClientIP on port 4444

  #Line 9 to 13 Same as "Server.py"
  commandwithipandport = s.recvfrom(1024)
  command = commandwithipandport[0]
  command = command.decode()
  clientip = commandwithipandport[1][0]

  #Connects the ClientIP with the Server Through ssh connections, Default Passwords should be used in companies for convinience
  clientname = command
  os.system("ssh" + " " + clientname + "@" + clientip )
