import os,sys
from hashlib import md5
from time import time

def generateAuth():
	os.system("sudo rm -rf /etc/3proxy/.proxyauth")
	with open('.proxyauth','w') as f:
		exit
		secret = md5(str(time())).hexdigest()
		secret = secret[0:6]+":CL:"+secret[10:16]
		f.write(secret)
		f.close()
		print "\n\nProxy authentication is:\n"+secret+"\n\n"
		return secret

def setUp():
	os.system("sudo apt-get update && apt-get -y upgrade")
	os.system("sudo apt-get install -y build-essential")
	os.system("rm 3proxy.cfg -f")
	os.system("rm 3proxyinit -f")
	os.system("rm 3proxy -f")
	os.system("/etc/init.d/3proxyinit stop")
	os.system("sudo rm -rf /etc/3proxy")
	os.system("sudo rm -f /etc/init.d/3proxyinit")
	os.system("sudo mkdir /etc/3proxy/")
	os.system("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/archive/3proxy.cfg")
	os.system("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/archive/3proxyinit")
	os.system("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/archive/3proxy")
	secret = generateAuth()
	os.system("sudo cp .proxyauth /etc/3proxy/.proxyauth")
	os.system("sudo cp 3proxy.cfg /etc/3proxy/3proxy.cfg")
	os.system("sudo mv 3proxy /etc/3proxy/")
	os.system("sudo mv 3proxyinit /etc/init.d/")
	os.system("sudo chmod a+x /etc/3proxy/3proxy")
	os.system("sudo chmod 600 /etc/3proxy/.proxyauth")
	os.system("sudo chmod 600 /etc/3proxy/3proxy.cfg")
	os.system("sudo chmod  +x /etc/init.d/3proxyinit")
	os.system("sudo update-rc.d 3proxyinit defaults")

def setPort():
	try:
		port = input("What port do yo want your proxy running at...???:\n")
	except Exception as e:
		port=8000
	if port==0:
		port = 8000
	os.system("sudo cp 3proxy.cfg /etc/3proxy/3proxy.cfg")
	with open('/etc/3proxy/3proxy.cfg','a') as f:
		f.write("\nproxy -n -p"+str(8000)+" -a")
		f.close()

if __name__ == '__main__':

	if len(sys.argv) == 1:
		setUp()
		setPort()
		os.system("sudo /etc/init.d/3proxyinit start")
	elif sys.argv[1] == 'setup':
		setUp()
	elif sys.argv[1] == 'start':
		secret = generateAuth()
		os.system("sudo cp .proxyauth /etc/3proxy/.proxyauth")
		os.system("sudo chmod 600 /etc/3proxy/.proxyauth")
		setPort()
		os.system("sudo /etc/init.d/3proxyinit start")
	elif sys.argv[1] == 'stop':
		os.system("sudo /etc/init.d/3proxyinit stop")
	elif sys.argv[1] == 'restart':
		secret = generateAuth()
		os.system("sudo cp .proxyauth /etc/3proxy/.proxyauth")
		os.system("sudo chmod 600 /etc/3proxy/.proxyauth")
		os.system("sudo /etc/init.d/3proxyinit stop")
		setPort()
		os.system("sudo /etc/init.d/3proxyinit start")
	elif sys.argv[1] == "showcred":
		try:
			f=  open('./etc/3proxy/.proxyauth')
			print f.read()
			f.close()
		except Exception as e:
			print "\nYou fucking shit. Setup first.\n"