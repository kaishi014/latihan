# fungsi (def) modularisasi

# Definisi fungsi aksi robot
def belok(arah, sudut):
    print(f"Robot belok ke {arah} sebesar {sudut} derajat.")

def cek_status(baterai):
    if baterai < 20:
        return "Bahaya"
    return "Aman"

# Memanggil fungsi
belok("kiri", 45)
status = cek_status(15)
print("Status baterai:", status)