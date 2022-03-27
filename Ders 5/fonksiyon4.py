#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek sonucunda True ya da False gönderen fonksiyonun python kodu
#kullanıcıadı: admin, şifre:123456 olmalı
def kontrol(kullanici,sifre):
    if kullanici=="admin" and sifre=="123456":
        return True
    else:
        return False
kullanici=input("Kullanıcı Adınızı Giriniz:")
sifre=input("Şifrenizi Giriniz:")
sonuc=kontrol(kullanici,sifre)
if sonuc==True:
    print("Doğru Girdiniz!")
else:
    print("Kullanıcı adı ve ya şifre hatalı") 