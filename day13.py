# kalkulator skor otomatis

skor_misi = []

# Menginput 3 nilai misi
for i in range(1, 4):
    nilai = int(input(f"Masukkan skor Misi {i}: "))
    skor_misi.append(nilai)

total_skor = sum(skor_misi)
print("\n--- HASIL PENILAIAN ---")
print("Total Skor:", total_skor)

# Penentuan kategori Kemenangan
if total_skor >= 250:
    print("Status: Predikat Emas (Lolos Sempurna)")
elif total_skor >= 180:
    print("Status: Predikat Perak")
else:
    print("Status: Perlu Evaluasi")