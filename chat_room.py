from socket import *
from Queue import Queue
import threading 

class ChatRoom:

	def __init__(self,hostname,portnum):
		self.host=hostname
		self.port=portnum
		
	def joinroom(self,chatrooms,roomname,clientname,roomref,join_id,connect):
		retmsg="JOINED_CHATROOM: room1\nSERVER_IP:%s\nPORT: 0\nROOM_REF: 1\nJOIN_ID: 0\n"%(serverip)
		connect.sendall(retmsg)
	
	def leaveroom(self):
		retmsg="LEFT_CHATROOM: room1\nJOIN_ID: 0\n"
		connect.sendall(retmsg)
	
	def disconnect(self):
		retmsg="DISCONNECT: 0\nPORT: 0\nCLIENT_NAME: Name\n"
		connect.sendall(retmsg)
		connection.close()
	def chat(self):
		retmsg="CHAT: 1\nCLIENT_NAME: Name\nMESSAGE: Hello\n"
		connect.sendall(retmsg)
