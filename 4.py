metin = input("Bir metin girin: ")
ters = ""

for harf in metin:
    ters = harf + ters  # Her harfi başa ekleyerek ters çevirir.

print(f"Ters hali: {ters}")
