import subprocess
sonuc=subprocess.check_output("ifconfig| grep 'inet addr'|grep 'Bcast'|cut -d ' ' -f12| cut -d ':' -f2",shell=True)
a= str(sonuc).split("\n")[0]
sorgu="echo "+a+" | nc 127.0.0.1 4444"
subprocess.call(sorgu,shell=True)
