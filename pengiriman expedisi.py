
#Program Perhitungan Biaya Pengirim Paket
#Layanan Ini Hanya Berlaku Di Kota Dan Kabupaten Pasuruan

def hitung_biaya_pengiriman(panjang, lebar, tinggi, berat):
  """
  Fungsi untuk menghitung biaya pengiriman paket.

  Args:
    panjang: Panjang paket dalam cm.
    lebar: Lebar paket dalam cm.
    tinggi: Tinggi paket dalam cm.
    berat: Berat paket dalam kg.

  Returns:
    Biaya pengiriman dalam rupiah.
  """

  #Tarif Biaya
  volume = panjang * lebar * tinggi
  biaya_tambahan = 50000 if volume > 50*50*50 else 0  # Biaya Tambahan Untuk Tarif Besar
  biaya_per_kg = 7000 if volume > 50*50*50 else 5000  # Biaya Untuk Paket Besar

  minimal_biaya = max(8000, biaya_per_kg * berat)     # Biaya Minimal Pengiriman
  total_biaya = biaya_dasar + biaya_tambahan          # Semua Total Biaya
  return total_biaya

# Ukuran Paket
panjang = float(input("Masukkan panjang paket (cm): "))
lebar = float(input("Masukkan lebar paket (cm): "))
tinggi = float(input("Masukkan tinggi paket (cm): "))
berat = float(input("Masukkan berat paket (kg): "))

#Menghitung Total Biaya
total_biaya = hitung_biaya_pengiriman(panjang, lebar, tinggi, berat)

#Total Biaya Pengiriman
print("Total biaya pengiriman: Rp", total_biaya)