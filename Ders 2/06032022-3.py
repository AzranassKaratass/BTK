#kullanıcıdan harf girmesini isteyiniz e girerse erekek k girerse kadın

cinsiyet=input("Bir harf giriniz E/K:")
if cinsiyet=="E" or cinsiyet=="e":
    print("Erkek")
elif cinsiyet=="K": #2. veya daha fazla şart olursa elif kullanılır
    print("Kadın")
else:
    print("Lütfen E veya K giriniz!")
print("Hoşçakalın...")