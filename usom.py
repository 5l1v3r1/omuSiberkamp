import subprocess
subprocess.check_output("wget https://www.usom.gov.tr/url-list.txt",shell=True)
dosya=open("url-list.txt","r")
icerik=dosya.readlines()
dosya.close()
site="askcopli.xyz"
for i in str(icerik).split("\n"):
	if site in i:
		print "Yanlis yerlere gidiyorsun"
