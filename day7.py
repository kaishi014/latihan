# struktur data (list)

# Menyimpan 4 sampel bacaan sensor
bacaan_sensor = [15, 12, 8, 20]

# Menambahkan data baru
bacaan_sensor.append(5)

print("Semua data sensor:", bacaan_sensor)
print("Data pertama:", bacaan_sensor[0])
print("Jumlah data:", len(bacaan_sensor))

# Mencari nilai terkecil (jarak terdekat)
print("Jarak terdekat yang terdeteksi:", min(bacaan_sensor), "cm")