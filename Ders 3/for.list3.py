#1'den 100'e kadar çift sayılar

for i in range(1,100):
    if i%2==0:
        print(i)

print("*.*")

for i in range(1,101):
    if i%2==0:
        print(i)

print("*.*")

for i in range(2,100,2):     #Adım sayısı ile her bir adımdaki artışı ayarlayabiliriz
    print(i)