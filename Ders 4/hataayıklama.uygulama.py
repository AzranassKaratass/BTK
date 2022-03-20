#Kullanıcıdan bir sayı girmesini isteyen,
#sayı girmediğinde tekrar tekrar sayı girmesini isteyen,
#sayı girdiğinde de ekrana sayının karesini yazdıran program
while True:
    try:
        sayi=int(input("Bir sayı giriniz:"))
        break
    except ValueError:
        print("Sadece sayıları kabul etmekteyim!")
print("Karesi:", sayi++2)