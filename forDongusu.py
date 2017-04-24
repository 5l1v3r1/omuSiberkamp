baslangic=raw_input("Baslangic sayisi: ")
bitis=raw_input("Bitis sayisi: ")
toplam=0
for i in range(int(baslangic),int(bitis)):
	if (i % 2) ==0: 
		print str(i)
		toplam=toplam+i
print "Sonuc: ",str(toplam)
