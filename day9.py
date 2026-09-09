# penggunaan library eksternal (time dan math)

import time
import math

# Menghitung jarak tempuh dari roda (Keliling = 2 * pi * r)
jari_jari = 3.5  # cm
rotasi_roda = 4
jarak_tempuh = rotasi_roda * (2 * math.pi * jari_jari)

print(f"Menghitung kalkulasi... Jarak: {jarak_tempuh:.2f} cm")

# Simulasi delay jeda eksekusi robot
print("Robot bersiap bergerak dalam...")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)  # Jeda 1 detik

print("MAJU!")