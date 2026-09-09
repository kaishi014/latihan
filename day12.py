# simulasi lomba

# Peta pergerakan robot (Daftar rintangan di depan dalam cm)
rintangan_lintasan = [30, 25, 12, 5, 40]

for jarak in rintangan_lintasan:
    print(f"\nJarak sensor: {jarak} cm")
    if jarak <= 10:
        print("-> Terlalu dekat! Putar balik / Cari jalan lain.")
        break  # Keluar dari lintasan / berhenti
    else:
        print("-> Aman, terus berjalan.")