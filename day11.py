# teknik debuging dengan log

def pemroses_navigasi(data_koordinat):
    print("[DEBUG] Memproses data koordinat...")
    
    for idx, titik in enumerate(data_koordinat):
        print(f"[DEBUG] Memeriksa titik index ke-{idx}: {titik}")
        
        if titik < 0:
            print(f"[ERROR] Titik tidak valid diabaikan: {titik}")
            continue
            
        print(f"[SUCCESS] Robot menuju titik: {titik}")

# Data uji coba
titik_tujuan = [10, 25, -5, 40]
pemroses_navigasi(titik_tujuan)