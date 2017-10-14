
class NiceColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

	def header(self, text):
		print(self.HEADER + text + self.ENDC)

	def ok(self, text):
		print(self.OKGREEN + text + self.ENDC)

	def ok2(self, text):
		print(self.OKBLUE + text + self.ENDC)

	def warning(self, text):
		print(self.WARNING + text + self.ENDC)

	def fail(self, text):
		print(self.FAIL + text + self.ENDC)

	def bold(self, text):
		print(self.BOLD + text + self.ENDC)

	def underline(self, text):
		print(self.UNDERLINE + text + self.ENDC)
