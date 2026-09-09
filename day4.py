# percabangan majemuk (elif dan operator logika)

jarak = int(input("Masukkan jarak objek (cm): "))
baterai = int(input("Sisa baterai (%): "))

# Pengecekan kondisi ganda
if baterai < 15:
    print("Aksi: Baterai lemah, kembali ke base!")
elif jarak < 10 and baterai >= 15:
    print("Aksi: Belok kanan untuk hindari halangan.")
else:
    print("Aksi: Jalan lurus.")