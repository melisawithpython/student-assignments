sayi = int(input("Bir sayı girin: ")) #kullanıcıdan sayı alır.
toplam = 0 

for i in range(1, sayi + 1): #sayılar birden başlayarak birer birer artar ve toplam değişkenine atanır.
    toplam += i

print(f"1'den {sayi}'ye kadar olan sayıların toplamı: {toplam}")
#f string ile çıktı ekrana yazdırılır.
