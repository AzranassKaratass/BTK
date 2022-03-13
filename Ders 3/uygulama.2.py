#kullanıcıadı ve şifre alınız. kullanıcı adı olarak "admin"
# şifre olarak 123456 girilince "sisteme başarıyla giriş yaptınız" yazsın
#yanlış girildikçe "kullanıcı adı veya şifre hatalı" yazıp tekrar kullanıcıadı ve şifre sorsun

while True:
    kullanıcıadı=input("Kullanıcı adınız:")
    sifre=input("Parolanız:")

    if kullanıcıadı=="admin" and sifre=="123456":
        break
else:
        print("kullanıcı adı veya parola hatalı")
print("sisteme başarıyla giriş yaptınız")