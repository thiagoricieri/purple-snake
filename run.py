from lib.utils import NiceColors
from lib.telnet_wrapper import RokuTalk

defaultHost = '10.7.7.0'

color = NiceColors()
talk = RokuTalk()
host = talk.hello()

try:
	talk.open(host)
	while True:
		try:
			info = talk.read()
			color.white(info)
		except KeyboardInterrupt:
			print("\n")
			color.fail("bye bye 👋")
			break

except ConnectionRefusedError:
	color.fail("Connection refused.")
