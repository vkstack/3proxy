import os
from hashlib import md5
from time import time

if __name__ == '__main__':
	# print secret,secret[0:16]+":C:"+secret[16:32]
	with open('.proxyauth','w') as f:
		secret = md5(str(time())).hexdigest()
		secret = secret[0:16]+":C:"+secret[16:32]
		f.write(secret)
		f.close()
		print secret
		# os.system("sudo apt-get update && apt-get -y upgrade")
		# os.system("sudo apt-get install -y build-essential nano")
		os.system("sudo cp .proxyauth /etc/3proxy/.proxyauth")
		os.system("rm 3proxy.cfg -f")
		os.system("rm 3proxyinit -f")
		os.system("rm 3proxy -f")
		os.system("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/archive/3proxy.cfg")
		os.system("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/archive/3proxyinit")
		os.system("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/archive/3proxy")
		os.system("sudo mkdir /etc/3proxy/")
		os.system("sudo mv 3proxy.cfg /etc/3proxy/")
		os.system("sudo mv 3proxy /etc/3proxy/")
		os.system("sudo mv 3proxyinit /etc/init.d/")
		os.system("sudo chmod 600 /etc/3proxy/.proxyauth")
		os.system("sudo chmod 600 /etc/3proxy/3proxy.cfg")
		os.system("sudo chmod  +x /etc/init.d/3proxyinit")
		# os.system("sudo cd /etc/init.d/")
		os.system("sudo update-rc.d 3proxyinit defaults")
		print "\n\n\n\n\nProxy authentication is:\n\n"+secret+"\n\n\n"
		