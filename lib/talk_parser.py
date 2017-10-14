
class RokuTalkParser:
	messages = []

	def consume(self, message):
		self.messages.append(message)

class DataWarehouseParser(RokuTalkParser):
	name = "DataWarehouseParser"

class RafParser(RokuTalkParser):
	name = "RafParser"
