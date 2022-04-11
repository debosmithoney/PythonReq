import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',1234))
print("Connection Established")

while True:
  msg=s.recv(1024)
  print("received:",msg.decode("utf-8"))
  m=str(input("Enter the message: "))
  s.send(m.encode("utf-8"))
  if m=='bye' or msg=='bye':
    break
s.close()