# perulangan while dan interaksi dengan pengguna

tombol_stop = False
detik = 1

# Loop berjalan selama tombol_stop bernilai False
while not tombol_stop:
    print(f"Robot beroperasi... Detik ke-{detik}")
    
    # Simulasi interaksi
    jawaban = input("Tekan 'x' untuk stop, tekan Enter untuk lanjut: ")
    if jawaban.lower() == 'x':
        tombol_stop = True
    
    detik += 1

print("Robot dimatikan.")