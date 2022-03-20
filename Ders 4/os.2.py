import os
while True:
    print("1- Klasör Oluştur")
    print("2- Klasör Sil")
    secim=input("Seçiminiz:")
    if secim=="1":
        ad=input("oluşturmak istediğiniz klasör adı giriniz:")
        for i in range(1,11):
             os.mkdir("elma"+ad(i))
    elif secim=="2":
        ad=input("silinicek klasör adı giriniz:")
        for i in range(1,11):
            os.rmdir(ad+str(i))

