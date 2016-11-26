import sys
from socket import *
from Queue import Queue
from threading import Thread


def messages(connect,msg):
	try:
		if msg[:13] == "JOIN_CHATROOM":
			retmsg="JOINED_CHATROOM: Chatroom\nSERVER_IP:0\nPORT:0\nROOM_REF:1\nJOIN_ID: 0\n"
			connect.sendall(retmsg)
		elif msg[:14] =="LEAVE_CHATROOM":
			retmsg="LEFT_CHATROOM: Chatroom\nJOIN_ID: 0\n"
			connect.sendall(retmsg)
		elif msg[:4] =="CHAT":
			retmsg="CHAT: 1\nCLIENT_NAME: Name\nMESSAGE: Hello\n"
			connect.sendall(retmsg)
		elif msg[:10] =="DISCONNECT":
			retmsg="DISCONNECT: 0\nPORT: 0\nCLIENT_NAME: Name\n"
			connect.sendall(retmsg)
			connection.close()
		elif msg[:4]=="HELO":
				print "HELO Received: "+receive
				msg="%sIP:%s\nPort:%s\nStudentID:13319829\n"%(msg,str(gethostbyname(gethostname())),int(sys.argv[2]))
				connect.sendall(msg)
				print "HELO Sent"
		else:
			errmsg="ERROR_CODE:1\nERROR_DESCRIPTION: Parse error\n"
			connect.sendall(errmsg)
			
	except Exception as error:	
		errmsg="ERROR_CODE:2\nERROR_DESCRIPTION: %s\n"%(error.message)
		connect.sendall(errmsg)


def chat_server(hostname,port_number,numb_of_threads):
	sock=socket(AF_INET,SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.bind((hostname,port_number))
	sock.listen(10)
	pool=Queue(numb_of_threads)
	threads=[]

	def handle(pool):
		while True:
			connect,address=pool.get()
			msg=connect.recv(2048)
			messages(connect,msg)

	try:
		for x in range(numb_of_threads):
			thread=Thread(target=handle,args=(pool,))
			thread.daemon=True
			thread.start()
			threads.append(thread)

		while True:
			connect,address=sock.accept()
			try:
				pool.put((connect,address),False)
			except Queue.Full:
				print("Queue full")
		sock.close()
	except(KeyboardInterrupt,SystemExit):
		sock.close()
		sys.exit(0)	


if __name__ == "__main__":
	chat_server(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
