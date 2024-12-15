#Program Perhitungan Biaya Parkir Terminal
def hitung_biaya_parkir(jam_parkir):
  """Fungsi untuk menghitung biaya parkir

  Args:
    jam_parkir: Jumlah jam kendaraan parkir    #Jumlah Jam Parkir

  Returns:
    Biaya parkir yang harus dibayarkan     #Biaya Yang Di Bayar
  """
   # Biaya 
  biaya_awal = 3000  # Biaya untuk 2 jam pertama
  biaya_tambahan_per_jam = 500  # Biaya tambahan per jam setelah 2 jam pertama
  biaya_tambahan_24_jam = 10000  # Biaya tambahan jika parkir lebih dari 24 jam

  if jam_parkir <= 2: #Jam Parkir
    return biaya_awal
  else:
    biaya_total = biaya_awal + (jam_parkir - 2) * biaya_tambahan_per_jam #Menghitung Semua Biaya
    if jam_parkir > 24:
      biaya_total += biaya_tambahan_24_jam
    return biaya_total #Semua Biaya

# Memasukkan Jam Parkir
jam_parkir = int(input("Masukkan jumlah jam parkir: "))
biaya = hitung_biaya_parkir(jam_parkir) #Menghitung Biaya
print("Biaya parkir yang harus dibayarkan adalah:", biaya) #total semua biaya