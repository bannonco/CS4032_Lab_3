from socket import *
from Queue import Queue
import threading 

class ChatRoom:

	def __init__(self,hostname,portnum):
		self.hostname=hostname
		self.portnum=portnum
		
	def joinroom(self,chatrooms,roomname,clientname,roomref,join_id,connect):
		if room_ref not in chatrooms:
			
			chatrooms[room_ref]={}
		if join_id not in chatrooms[room_ref]:
			print("here")
			chatrooms[room_ref][join_id]=connect
			retmsg="JOINED_CHATROOM:%s\nSERVER_IP:%s\nPORT:%s\nROOM_REF:%s\nJOIN_ID:%s\n"%(roomname,self.hostname,self.portnum,roomref,join_id)
			connect.sendall(retmsg)
	
	def leaveroom(self,chatrooms,room_ref,join_id,clientname,connect):
	
		retmsg="LEFT_CHATROOM:%s\nJOIN_ID:%s\n"%(str(roomref),str(join_id))
		connect.sendall(retmsg)
		del chatrooms[room_ref][join_id]
	
	def disconnect(self,chatrooms,join_id,clientname,connect):
		for room in chatrooms.keys():
			if join_id in chatrooms[join_id]:
				retmsg="DISCONNECT: 0\nPORT: 0\nCLIENT_NAME: Name\n"
				connect.sendall(retmsg)
				del chatrooms[room][join_id]
	def chat(self,chatrooms,room_ref,join_id,clientname,msg,connect):
		retmsg="CHAT:%s\nCLIENT_NAME:%s\nMESSAGE:%s\n\n"%(str(room_ref),str(clientname),msg)
		connect.sendall(retmsg)
