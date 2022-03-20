import random
while True:
    seviye=input("Bir seviye seçiniz: kolay/orta/zor/ultra zor")
    if seviye=="kolay":
       uret=random.randint(1,15)
       break
    elif seviye=="orta":
       uret=random.randint(1,65)
       break
    elif seviye=="zor":
       uret=random.randint(1,145)
    elif seviye=="ultra zor":
       uret=random.randint(1,235)
while True:
    tahmin=int(input("Bir tahminde bulununuz:"))
    if tahmin<uret:
        print("Sayınızı büyültün!")
    elif tahmin>uret:
        print("Sayınızı küçültün")
    else:
        print("Tebrikler, bildiniz!")
        break
