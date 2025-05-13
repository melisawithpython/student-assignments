import pandas as pd



# CSV dosyası projeye eklendi.
data = pd.read_csv("train.csv")

# İlk 5 satırı yazdır
print(data.head())

# Veri seti hakkında bilgi
print(data.info())

# Hayatta kalma oranı
print(data['Survived'].value_counts(normalize=True))

#eksik verilerin toplamı
print(data.isnull().sum())

#istatiksel özet
print(data.describe())






