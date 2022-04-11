import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',1234))
s.listen(1)
print ("waiting for connection")
conn, addr = s.accept()
print ("connected to:", addr)
while True:
  m=str(input("Enter the message: "))
  conn.send(m.encode("utf-8"))
  data=conn.recv(1024)
  print("received:",data.decode("utf-8"))
  if m=='bye' or data=='bye':
    break
s.close()