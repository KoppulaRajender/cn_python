import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',6767))
s.listen(5)
client,address=s.accept()
while True:
	str1=client.recv(1024)
	num=int(str1)
	result=num*2
	if str1=="bye" or str1=="exit":
		print"exiting"
		client.send("exit")
		break
	else:
		result=str(result)
		client.send(result)
	
	
			
