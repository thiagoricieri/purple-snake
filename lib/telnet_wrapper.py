import telnetlib

class RokuTalk:

	def __init__(self):
		self.telnet = telnetlib.Telnet()

	def open(self, host="", port=8085):
		self.telnet.open(host, port)

	def read(self):
		out = self.telnet.read_until(b"\n", 5)
		return out.decode("UTF-8").strip()

	def close(self):
		self.telnet.close()
