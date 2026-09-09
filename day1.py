# input, output dan tipe data

# Membaca data dari sensor (input)
nama_robot = input("Masukkan nama robot: ")
jarak_str = input("Masukkan jarak halangan (cm): ")

# Konversi string ke integer (angka bulat)
jarak = int(jarak_str)

# Output hasil
print("Robot", nama_robot, "mendeteksi objek pada jarak:", jarak, "cm")