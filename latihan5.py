print("=== GEROBAK FRIED CHICKEN ===")
print("Daftar Harga Ayam Goreng:")
print("Kode\tJenis Potong\tHarga")
print("----------------------------------")
print("D\tDada\t\tRp. 2500")
print("P\tPaha\t\tRp. 2000")
print("S\tSayap\t\tRp. 1500")
print("----------------------------------") 

harga_dict = {'D': 2500, 'P': 2000, 'S': 1500}
nama_dict = {'D': 'Dada', 'P': 'Paha', 'S': 'Sayap'}

banyak_jenis = int(input("Masukkan banyak jenis potong yang dibeli: "))

# Simpan data pesanan
pesanan = []
total_harga = 0

for i in range(banyak_jenis):
    jenis_potong = input("Masukkan kode jenis potong: ").upper()
    banyak_beli = int(input("Masukkan banyak beli: "))
    harga = harga_dict[jenis_potong] * banyak_beli
    total_harga += harga
    
    # Simpan pesanan
    pesanan.append({
        'kode': jenis_potong,
        'nama': nama_dict[jenis_potong],
        'jumlah': banyak_beli,
        'harga': harga
    })

pajak = total_harga * 0.1
total_bayar = total_harga + pajak

# Struk pembayaran sederhana
print("\n=== STRUK PEMBAYARAN ===")
print("-------------------------")
print("Pesanan Anda:")
for item in pesanan:
    print(f"Jenis Potong\t: {item['nama']}")
    print(f"Banyak Beli\t: {item['jumlah']}")
    print(f"Harga\t\t: Rp. {item['harga']}")
    print()
print("-------------------------")
print("Total Harga\t: Rp.", total_harga)
print("Pajak (10%)\t: Rp.", int(pajak))
print("Total Pembayaran: Rp.", int(total_bayar))
print("=========================")