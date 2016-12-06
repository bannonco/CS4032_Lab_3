import sys
from socket import *
from Queue import Queue
from threading import Thread
import collections
from chat_room import ChatRoom
from random import randint

chat_room=ChatRoom(sys.argv[1],int(sys.argv[2]))
rooms=collections.OrderedDict()
active=True

def messages(connect,msg):
	while active
		try:
			if msg[:13] == "JOIN_CHATROOM":
				print("joining chatroom")
				msgs=msg.split("\n")
				chatroom=msgs[0].split(":")[1]
				client_name=msgs[3].split(":")[1]
				room_ref=
				join_id=randint(0,100)
				chat_room.joinroom(rooms,chatroom,clientname,room_ref,join_id,connect)
				print("joined chatroom")
			elif msg[:14] =="LEAVE_CHATROOM":
				print("leaving chatroom")
				msgs=msg.split("\n")
				room_ref=int(msgs[0].split(":")[1])
				join_id=int(msgs[1].split(":")[1])
				client_name=msgs[2].split(":")[1]
				chat_room.leaveroom(rooms,room_ref,join_id,client_name,connect)
				print("left chatroom")
			elif msg[:10] =="DISCONNECT":
				print("client disconnecting")
				msgs=msg.split("\n")
				client_name=msgs[2].split(":")[1]
				chat_room.disconnect(rooms,client_name,connect)
				print("client disconnected")	
				active=False
			elif msg[:4] =="CHAT":
				print("received message")
				msgs=msg.split("\n")
				room_ref=int(msgs[0].split(":")[1])
				join_id=int(msgs[1].split(":")[1])
				client_name=msgs[2].split(":")[1]
				data=msgs[3].split(":")[1]
				chat_room.chat(rooms,room_ref,join_id,client_name,data,connect)				
				print("message received")
			elif msg[:4]=="HELO":
					print "HELO Received: "+msg
					msg="%sIP:%s\nPort:%s\nStudentID:13319829\n"%(msg,str(gethostbyname(gethostname())),int(sys.argv[2]))
					connect.sendall(msg)
					print "HELO Sent"
			elif msg[:12]=="KILL_SERVICE":				
					connect.sendall("KILLED!!")
					connect.shutdown(SHUT_RDWR)
					connect.close()
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
