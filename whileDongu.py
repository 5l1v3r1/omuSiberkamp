baslangic=int(raw_input("Baslangic: "))
bitis=int(raw_input("Bitis: "))
toplam=0
while (baslangic<bitis):
	if (baslangic % 2)==0:
		print str(baslangic)
		#baslangic=baslangic+1
		toplam=toplam+baslangic
	baslangic=baslangic+1
print "Sonuc:",str(toplam)
