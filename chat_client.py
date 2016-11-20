from socket import *
from Queue import Queue
import threading 


##class Chat_Client:
def console(q, lock):
    while 1:
	input()   
	with lock:
	    cmd = input('> ')

	q.put(cmd)
	if cmd == 'quit':
	    break

def join(self,lock):
	with lock:
		msg="JOIN_CHATROOM: chatroom\nCLIENT_IP: 0\nPORT: 0\nCLIENT_NAME:%s\n"%(self.handle)
		self.sock.sendall(msg)
		resp=self.sock.recv(2048)

def leave(self,room_ref,lock):
	with lock:
		msg="LEAVE_CHATROOM: %s\nJOIN_ID: %s\nCLIENT_NAME:%s\n"%(room_ref,self.client_id,self.handle)
		self.sock.sendall(msg)
		resp=self.sock.recv(2048)

def sendmsg(self,room_ref,msg,lock):
	with lock:
		msg="CHAT:%s \nJOIN_ID: %s\nCLIENT_NAME: %s\nMESSAGE:%s\n\n"%(room_ref,self.client_id,self.handle,msg)
		self.sock.sendall(msg)
		resp=self.sock.recv(2048)

def disconnect(self,lock):
	with lock:
		msg="DISCONNECT: 0\nPORT: 0\nCLIENT_NAME:%s\n"%(self.handle)
		self.sock.sendall(msg)
		resp=self.sock.recv(2048)

def invalid_input(lock):
	with lock:
		print('--> Unknown command')


def main():
	port_num=8000
	handle='chat0'
	msgs=[]
	client_id=0
	sock=socket(AF_INET,SOCK_STREAM)
	sock.connect(('0.0.0.0',port_num))
	cmd_actions={'j':join,'l':leave,'chat':sendmsg,'dis':disconnect}
	cmd_queue=Queue()
	stdout_lock=threading.Lock()
	dj = threading.Thread(target=console, args=(cmd_queue, stdout_lock))
	dj.start()
    	while 1:
			cmd = cmd_queue.get()
			if cmd == 'quit':
				break
			action = cmd_actions.get(cmd, invalid_input)
			action(stdout_lock)		

	

main()
