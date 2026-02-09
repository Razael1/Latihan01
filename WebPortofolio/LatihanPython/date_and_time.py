import datetime
skrg =datetime.date.today()
print(skrg)
hari = (f'hari = {skrg:%A}')
print(hari)
tanggal =datetime.date(2001,9,11)
print(tanggal)


'''print('masukkan tanggal lahir anda')
tanggal = int(input('tanggal lahir : '))
bulan = int(input('bulan lahir : '))
tahun = int(input('tahun lahir : '))
lahir = datetime.date(tahun,bulan,tanggal)
umur = skrg - lahir
umur_tahun = umur.days // 365
bulan_sisa = umur.days % 365 //30
print(f'umurmu = {umur_tahun} tahun lebih {bulan_sisa} bulan')'''

#Weton

tanggal = int(input('tanggal : '))
bulan = int(input('bulan : '))
tahun = int(input('tahun : '))
tanggal_input = datetime.date(tahun,bulan,tanggal)
tanggal_awal = datetime.date(1, 1, 1)
selisih_hari = (tanggal_input - tanggal_awal).days

weton = ["pahing", "pon", "wage", "kliwon", "legi"]
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

indeks_weton = selisih_hari % 5
indeks_hari = selisih_hari % 7

print(f"Weton : {hari[indeks_hari]} {weton[indeks_weton]}")

