import os

os.call("sudo apt-get update && apt-get -y upgrade")
os.call("sudo apt-get install -y build-essential nano")
# os.call("sudo wget --no-check-certificate https://github.com/z3APA3A/3proxy/archive/3proxy-0.8.6.tar.gz")
# os.call("sudo tar xzf 3proxy-0.8.6.tar.gz")
# os.call("sudo cd 3proxy-3proxy-0.8.6")
# os.call("sudo make -f Makefile.Linux")
# os.call("sudo cd src")
os.call("sudo mkdir /etc/3proxy/")
# os.call("sudo mv 3proxy /etc/3proxy/")
os.call("sudo cd /etc/3proxy/")
os.call("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/3proxy.cfg")
os.call("sudo chmod 600 /etc/3proxy/3proxy.cfg")
# os.call("sudo wget --no-check-certificate https://github.com/barankilic/3proxy/raw/master/.proxyauth")
with open('.proxyauth','w') as f:

os.call("sudo chmod 600 /etc/3proxy/.proxyauth")
os.call("sudo cd /etc/init.d/")
os.call("sudo wget --no-check-certificate https://raw.githubusercontent.com/vkstack/3proxy/master/3proxyinit")
os.call("sudo chmod  +x /etc/init.d/3proxyinit")
os.call("sudo update-rc.d 3proxyinit defaults")