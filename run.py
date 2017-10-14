from lib.utils import NiceColors
from lib.telnet_wrapper import RokuTalk

defaultHost = '10.7.7.0'
host = input('What\'s the host? (default = '+defaultHost+') ')

if host == None or host == "":
	host = defaultHost
	print("... using default host.")

color = NiceColors()
talk = RokuTalk()
talk.open(host)

while True:
	info = talk.read()
	color.ok(info)

talk.close()
