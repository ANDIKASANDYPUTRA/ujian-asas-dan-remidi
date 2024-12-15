# Program Perhitungan Biaya Parkir untuk Sepeda Motor dan Mobil

# Fungsi untuk menghitung biaya parkir
def hitung_biaya_parkir(lama_parkir, jenis_kendaraan):
    """
    Menghitung biaya parkir berdasarkan jenis kendaraan dan lama parkir.
    Tarif:
    - 2 jam pertama: Rp 3.000
    - Lebih dari 2 jam:
      - Motor: Rp 1.000 per jam tambahan
      - Mobil: Rp 1.500 per jam tambahan
    - Lebih dari 24 jam: Tambah biaya Rp 10.000
    """
    # Biaya dasar 2 jam pertama
    biaya = 3000
    
    # Hitung biaya tambahan jika melebihi 2 jam
    if lama_parkir > 2:
        if jenis_kendaraan == "motor":
            biaya += (lama_parkir - 2) * 1000
        elif jenis_kendaraan == "mobil":
            biaya += (lama_parkir - 2) * 1500
        else:
            print("Jenis kendaraan tidak valid!")
            return None  # Keluar jika jenis kendaraan tidak valid
    
    # Tambah biaya jika parkir lebih dari 24 jam
    if lama_parkir > 24:
        biaya += 10000
    
    return biaya

# Program utama
def main():
    print("Program Perhitungan Biaya Parkir Stasiun")
    print("---------------------------------------")
    print("Jenis kendaraan: motor / mobil")
    
    # Input: Jenis kendaraan dan lama parkir
    jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ").strip().lower()
    try:
        lama_parkir = int(input("Masukkan lama parkir (dalam jam): "))
        
        # Validasi input lama parkir
        if lama_parkir <= 0:
            print("Lama parkir harus lebih dari 0 jam.")
            return
        
        # Hitung biaya parkir
        total_biaya = hitung_biaya_parkir(lama_parkir, jenis_kendaraan)
        
        # Tampilkan hasil jika jenis kendaraan valid
        if total_biaya is not None:
            print(f"Total biaya parkir untuk {jenis_kendaraan} selama {lama_parkir} jam adalah Rp {total_biaya}")
    
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk lama parkir!")

# Jalankan program utama
if __name__ == "__main__":
    main()