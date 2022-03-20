liste=[2, 4 ,"a", 87, "5b", "51"]
#Soru: yukarıdaki listenin sadece int olanlarını try except ile ekrana yazdırınız
for i in liste:
     try:
         print(int(i))
     except:
         pass
