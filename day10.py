# algoritma keputusan (simulasi)

# 0 = Putih (Lintasan), 1 = Hitam (Garis Pembatas)
sensor_kiri = int(input("Input Sensor Kiri (0/1): "))
sensor_kanan = int(input("Input Sensor Kanan (0/1): "))

if sensor_kiri == 0 and sensor_kanan == 0:
    print("Aksi: Lurus maju presisi")
elif sensor_kiri == 1 and sensor_kanan == 0:
    print("Aksi: Koreksi! Koreksi ke Kiri")
elif sensor_kiri == 0 and sensor_kanan == 1:
    print("Aksi: Koreksi! Koreksi ke Kanan")
else:
    print("Aksi: Garis finish/Perempatan terdeteksi! STOP")