#print(a) #nameerror hatası

#print("Btk" deneme) #syntax error

#print(10/0) #zeroDivisionError hatası verir

#int("5a") #valueError hatası verir

try:
    sayi=int(input("Bir sayı giriniz:"))
    sayi2=int(input("Bir sayı giriniz:"))
    print("Bölüm:", sayi/sayi2)
except ValueError:
    print("Lütfen sayı gir! Harf girme!")
except ZeroDivisionError:
    print("0'a bölme yapılamaz!")
except SyntaxError:
    print("Yazım hatan var!")
except NameError:
    print("Böyle bir değişken yok!")
except:
    print("Genel bir hata oluştu")
print("Program buradan çalışmasına devam eder...")