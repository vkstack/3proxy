# https://github.com/benjamin74/3proxy
apt-get update && apt-get -y upgrade
apt-get install -y build-essential nano
# wget --no-check-certificate https://github.com/barankilic/3proxy/blob/master/archive/3proxy-3proxy-0.8.6.tar.gz
# tar xzf 3proxy-0.8.6.tar.gz
# cd 3proxy-3proxy-0.8.6
# make -f Makefile.Linux
# cd src
# mkdir /etc/3proxy/
mv 3proxy /etc/
chmod -R 600 /etc/3proxy
mv 3proxyinit /etc/init.d/3proxyinit
chmod 600 /etc/init.d/3proxyinit
cd /etc/init.d/
chmod  +x /etc/init.d/3proxyinit
update-rc.d 3proxyinit defaults