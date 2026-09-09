## Minggu 1: Fondasi Logika & Algoritma Lomba

### Day 1: Input, Output, & Tipe Data

* **Cara Menjelaskan:**
> *"Bayangkan robot itu punya **mata** dan **mulut**. Input itu matanya (membaca keadaan sekitar), Output itu mulutnya (menampilkan informasi). Masalahnya, komputer menganggap semua masukan dari keyboard sebagai **teks**. Kalau kita mau hitung jarak, teks '10' harus kita ubah jadi angka `10` pakai perintah `int()`."*


* **Langkah Praktik:** Minta mereka buat program menyapa nama robot dan mengubah input angka jarak dari teks ke `int`.

### Day 2: Operator Aritmatika & Type Casting (`float`)

* **Cara Menjelaskan:**
> *"Sensor robot di dunia nyata itu tidak presisi angka bulat, kadang hasilnya desimal seperti 10,5 cm. Makanya kita pakai `float()`. Hari ini kita belajar cara bikin robot pinter berhitung—misal menghitung rata-rata dari dua sensor ultrasonik."*


* **Langkah Praktik:** Pandu mereka menjumlahkan dua nilai `float` lalu membaginya dengan angka 2.

### Day 3: Percabangan Dasar (`if-else`)

* **Cara Menjelaskan:**
> *"Robot itu tidak punya otak, kita yang kasih tahu otaknya harus mikir apa. Logikanya sederhana: **JIKA** ada halangan di bawah 10 cm, **MAKA** berhenti. **JIKA TIDAK**, jalan terus. Di Python, kita pakai perintah `if` dan `else`."*


* **Langkah Praktik:** Minta mereka mengetik kode percabangan dan mencoba memasukkan angka jarak yang berubah-ubah di layar terminal.

### Day 4: Percabangan Majemuk (`elif` & `and`)

* **Cara Menjelaskan:**
> *"Di arena lomba, keputusan robot nggak cuma 'ya' dan 'tidak'. Bisa saja: JIKA baterai habis, pulang. JIKA baterai aman DAN ada halangan, belok. JIKA aman semua, jalan lurus. Pilihan tambahan ini pakai `elif`, dan syarat ganda pakai `and`."*


* **Langkah Praktik:** Tulis skenario logika di papan/kertas, lalu minta mereka menerjemahkannya ke dalam baris `if-elif-else`.

### Day 5: Perulangan `while` (Main Loop Robot)

* **Cara Menjelaskan:**
> *"Robot di arena itu bernapas dalam **Looping**. Selama sakelar menyala (kondisi True), dia bakal terus ngecek sensor berulang-ulang tanpa berhenti. Begitu tombol 'Stop' ditekan, loop-nya pecah/berhenti."*


* **Langkah Praktik:** Buat program `while` yang terus berjalan sampai peserta mengetik huruf `'x'`.

### Day 6: Perulangan `for` & `range()`

* **Cara Menjelaskan:**
> *"Bedanya sama `while`, perulangan `for` itu kita sudah tahu mau diulang berapa kali. Misal: 'Robot, jalan 5 langkah ke depan!'. Kita pakai `range(1, 6)` untuk menghitung dari langkah ke-1 sampai ke-5."*


* **Langkah Praktik:** Suruh mereka membuat program yang menampilkan hitungan langkah otomatis dari 1 sampai 10.

### Day 7: List (Memori Penyimpanan Robot)

* **Cara Menjelaskan:**
> *"Bagaimana kalau robot harus mengingat 5 pembacaan sensor terakhir? Nggak mungkin kita bikin 5 variabel beda. Kita pakai **List**—ibarat kotak perkakas tempat nyimpan banyak data sekaligus."*


* **Langkah Praktik:** Buat list berisi [15, 12, 8, 20], lalu tunjukkan cara mengambil angka paling kecil memakai `min()`.

---

## Minggu 2: Pola Soal Lomba & Simulasi Robotik

### Day 8: Fungsi (`def`)

* **Cara Menjelaskan:**
> *"Daripada kamu ngetik 10 baris kode yang sama berulang kali saat robot mau belok, mending kode itu dibungkus jadi satu tombol resep bernama `def belok()`. Setiap butuh belok, tinggal panggil nama fungsinya."*


* **Langkah Praktik:** Pandu mereka buat fungsi `def belok_kiri()` yang isinya beberapa perintah cetak.

### Day 9: Library `time` & `math`

* **Cara Menjelaskan:**
> *"Python punya kotak alat tambahan bernama **Library**. Kalau butuh jeda waktu (delay), kita `import time`. Kalau butuh rumus matematika rumit (seperti menghitung keliling roda), kita `import math`."*


* **Langkah Praktik:** Bikin simulasi *countdown* (hitung mundur) 3, 2, 1 menggunakan `time.sleep(1)`.

### Day 10: Logika Line Follower

* **Cara Menjelaskan:**
> *"Ini simulasi asli lomba! Robot punya sensor kiri dan kanan. Angka 0 = Karpet Putih, Angka 1 = Garis Hitam. Tugas kalian: bikin logika `if-elif` supaya kalau sensor kiri kena angka 1, robotnya harus belok kiri."*


* **Langkah Praktik:** Berikan tabel logika (0 dan 1), lalu minta mereka mengodekan semua kombinasi kemungkinan pergerakan robot.

### Day 11: Debugging (Melacak Kesalahan)

* **Cara Menjelaskan:**
> *"Saat lomba, kadang sensor suka error dan kasih angka aneh (misal angka minus). Hari ini kita belajar cari gara-gara (debugging) dan mengabaikan data rusak itu pakai perintah `continue`."*


* **Langkah Praktik:** Kasih mereka baris kode yang ada nilai salahnya, lalu ajari cara menambahkan `print("[DEBUG]")` untuk melacak baris mana yang error.

### Day 12: Navigasi Labirin (`break`)

* **Cara Menjelaskan:**
> *"Robot menyusuri deretan data lorong labirin menggunakan `for`. Tapi kalau tiba-tiba di tengah jalan ketemu tembok rapat, robot harus **STOP seketika** dan keluar dari perulangan. Perintahnya pakai `break`."*


* **Langkah Praktik:** Buat list urutan lorong dan minta mereka menghentikan program di pertengahan jalan pakai kondisi `if` + `break`.

### Day 13: Kalkulator Skor Lomba

* **Cara Menjelaskan:**
> *"Hari ini kita belajar logika untuk juri atau sistem scoring lomba. Program membaca 3 nilai misi, menjumlahkannya pakai `sum()`, lalu menentukan tim kita dapat Medali Emas, Perak, atau Perunggu."*


* **Langkah Praktik:** Buat program interaktif yang meminta input 3 nilai, menampilkannya rapi, dan mencetak status kemenangan.

### Day 14: Tryout & Mentoring Mental

* **Cara Menjelaskan:**
> *"Hari ini tidak ada materi baru. Ini simulasi tanding! Saya kasih 1 soal cerita gabungan, kalian selesaikan dalam waktu 30 menit tanpa melihat catatan. Jangan panik kalau ketemu error, baca pesan error-nya pelan-pelan."*


* **Langkah Praktik:** Beri soal kasus (misal: gabungan pembacaan sensor + `if` + `while`), lalu amati cara mereka koding secara mandiri. Beri masukan di akhir session.