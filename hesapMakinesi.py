# -*- coding: utf-8 -*-
islem=raw_input("İslemi giriniz :")
sayi1=raw_input("Birinci sayiyi giriniz: ")
sayi2=raw_input("İkinci sayiyi girniz: ")
if islem=="1":
	sonuc=int(sayi1)+int(sayi2)
	print "Sonuc: ",str(sonuc)
elif islem=="2":
	sonuc=int(sayi1)-int(sayi2)
	print "Sonuc: ",str(sonuc)
elif islem=="3":
	sonuc=int(sayi1)*int(sayi2)
	print "Sonuc: ",str(sonuc)
elif islem=="4":
	sonuc=int(sayi1)/int(sayi2)
	print "Sonuc: ",str(sonuc)
