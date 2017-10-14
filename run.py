from lib.utils import NiceColors
from lib.telnet_wrapper import RokuTalk
from lib.talk_parser import DataWarehouseParser, RafParser

defaultHost = '10.7.7.0'

log = NiceColors()

# Talk
talk = RokuTalk()
host = talk.whats_your_host()

# Parsers
rafParser = RafParser()
dataParser = DataWarehouseParser()

try:
	talk.open(host)
	while True:
		try:
			info = talk.read()
			dataParser.consume(info)
			if info is not None or info != "":
				log.clear()
			log.white(info)

		except KeyboardInterrupt:
			log.clear()
			log.fail("bye bye 👋")
			break

except ConnectionRefusedError:
	color.fail("Connection refused.")
