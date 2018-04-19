#!/usr/bin/python

import os
import urllib2

suricatadirectory='/etc/suricata/'
md5file=suricatadirectory+'lastmd5'
rulesdirectory=suricatadirectory+'rules.tar.gz'
rulesurl='https://rules.emergingthreats.net/open-nogpl/suricata-2.0/emerging.rules.tar.gz'


#Actualizacion de reglas
def deploynewrules():
	os.system("wget " + rulesurl + " -o /tmp/wget.output -O" + rulesdirectory)
	os.system("tar -xzf " + rulesdirectory + " -C " + suricatadirectory)

#Comprobar si ha cambiado el md5
def md5change():
	re = urllib2.urlopen(rulesurl+".md5")
	newmd5 = re.read()

	oldmd5file = open(md5file,"r")
	oldmd5 = oldmd5file.read()
	oldmd5file.close()

	if newmd5!=oldmd5 :
		md5 = open (md5file,"w")
		md5.write(newmd5)
		md5.close()
		return 1

	else:
		return 0

def main():     
	if os.path.exists(md5file):
		if md5change():
			deploynewrules()
	else:
		re = urllib2.urlopen(rulesurl+".md5")
		newmd5 = re.read()
		md5 = open (md5file,"w")
		md5.write(newmd5)
		md5.close()
		deploynewrules()


if __name__ == '__main__':
	main()
