import getpass
import sys
import telnetlib

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

host = "10.7.7.0"
telnet = telnetlib.Telnet()
telnet.open(host, 8085)
while True:
	out = telnet.read_until(b"\n", 5)
	print(bcolors.WARNING + out.decode("UTF-8") + bcolors.ENDC)
telnet.close()
