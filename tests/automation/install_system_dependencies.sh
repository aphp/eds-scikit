# install java for pyspark
# see https://stackoverflow.com/questions/57031649/how-to-install-openjdk-8-jdk-on-debian-10-buster
apt-get update
apt-get install -y software-properties-common
apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main'
apt-get update
apt-get install -y openjdk-8-jdk
