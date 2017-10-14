import telnetlib

class RokuTalk:

	defaultHost = "10.7.7.0"

	def __init__(self, defaultHost=None):
		self.telnet = telnetlib.Telnet()
		if defaultHost != None:
			self.defaultHost = defaultHost

	def whats_your_host(self):
		result = self.ask('👨‍💻 What\'s the host? (default = '+self.defaultHost+')')
		if result is None or result == "":
			result = self.defaultHost
		return result

	def ask(self, message):
		result = input(message)
		return result

	def open(self, host="", port=8085):
		self.telnet.open(host, port)

	def read(self):
		out = self.telnet.read_until(b"\n", 2)
		return out.decode("UTF-8").strip()

	def close(self):
		self.telnet.close()
