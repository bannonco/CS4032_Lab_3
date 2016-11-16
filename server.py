from socket import *
from threading import Thread
from Queue import Queue
import sys


def messages_handler(connect,msg)
	try:
		if msg[:13] == "JOIN_CHATROOM":
			##
		elif msg[:14] =="LEAVE_CHATROOM":
			##
		elif msg[:4] =="CHAT":
			##
		elif msg[:10] =="DISCONNECT":
			##
		else:
			connect.sendall("Parse error")
	except Exception as error:
		errmsg=error.message
		connect.sendall(errmsg)


def chat_server(hostname,port_number,numb_of_threads)
	sock=socket(AF_INET,SOCK_STREAM)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	pool=Queue(numb_of_threads)



if __name__ == "__main__":
	chat_server(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
