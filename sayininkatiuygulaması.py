import math
import random
x=int(input("0 ile 100 Arasında Kaç Tane Sayı Üretilsin?:"))
for a in range(x):
       rand = int(random.randint(1, 101))

secim=input("2'nin katını bulmak için--1")
if secim=="1":
    rand = int(random.randint(1, 101))
    if rand % 2 == 1:
        print("2'nin katı değildir:", rand)
    else:
        print("2'nin katıdır:", rand)
else:
        print("Geçerli Giriş Yapınız")




