#kullanıcıdan 5 tane sayı isteyerek en büyük sayıyı listeye atayarak bulunuz!
sayi1=input("1. sayıyı giriniz:")
sayi2=input("2. sayıyı giriniz:")
sayi3=input("3. sayıyı giriniz:")
sayi4=input("4. sayıyı giriniz:")
sayi5=input("5. sayıyı giriniz:")
sayilar=[]
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.append(sayi5)
sayilar.sort()
print("Girdiğiniz sayılardan en büyüğü:,sayılar[4]")