'''#menyambung string (concatenate)
awal = 'see'
tengah = 'deez'
akhir = 'nuts'
print(awal + tengah + akhir)
print(awal + ' ' + tengah + ' ' + akhir)
awal = 'see '
tengah = 'deez '
akhir = 'nuts'
print(awal + tengah + akhir)
lengkap = awal + tengah + akhir
print(lengkap)

data = 'and if a double decker bus'

#menghitung panjang string
panjang = len(data)
print('jumlah karakter pada data adalah = ',panjang)

#mengecek apakah ada suatu char dalam string
e = 'e'
status = e in data
print('status huruf e pada data adalah = ',status)
status = e not in data
print('status tidak ada huruf e pada data adalah = ',status)

#mengulang string
print('wk'*10)

#indexing
print('indeks ke 0 = ' + data[0])
print('indeks ke 16 = ' + data[16])
print('indeks ke -1 = ' + data[-1]) #balik ke belakang
print('indeks ke 0-26 = ' + data[0:26])
print('indeks ke 0,2,4,6,8,10 = ' + data[0:10:2])

#item paling kecil dan besar
print('paling kecil = ' + min(data))
print('paling besar = ' + max(data))

#ASCII code
ascii_code = ord('D')
print('ASCII code untuk D adalah = ', str(ascii_code))
entah = 75
print('char untuk ASCII 75 adalah = ',chr(entah))'''


#OPERATOR DENGAN METHODS

#DATA COUNT
data = 'and if a double decker bus'
datacount = data.count('d')
print('jumlah huruf d pada kata "' + data + '" = ', datacount)

#Merubah ke lowercase dan uppercase
deez = 'Deez Nuts On Your Face'
uppercase = deez.upper ()
lowercase = deez.lower ()
print(deez)
print('uppercase = ',uppercase)
print('lowercase = ',lowercase)

#MENGECEK APAKAH HANYA TERDIRI DARI SUATU KARAKTER
huruf = deez.isalpha () #huruf
angka = deez.isdecimal () #angka
gabungan = deez.isalnum () #gabungan huruf dan angka
space = deez.isspace () #tab,space,enter(\n)
title = deez.istitle () #diawali huruf besar
print(huruf)
print(angka)
print(gabungan)
print(space)
print(title)

#CEK KOMPONEN START DAN END
print('==============')
cek_start = 'Ray Piece'.startswith('Ray')
cek_end = 'Ray Piece'.endswith('Piece')
print('Ray Piece')
print('start = ' + str(cek_start))
print('end = ' + str(cek_end))

#PENGGABUNGAN DAN PEMISAHAN
pisah = ['Moe','lester']
gabung = ' '.join(pisah)
print(gabung)

gabung = 'Moe lester'
print(gabung.split(' '))

#ALOKASI KARAKTER
kanan ='kanan'.rjust(10)
print("'" + kanan + "'")
kiri ='kiri'.ljust(10)
print("'" + kiri + "'")
tengah ='tengah'.center(10)
print("'" + tengah + "'")
tengah ='tengah'.center(20,'=')
print("'" + tengah + "'")

#menghilangkan karakter (strip)
ditengah = tengah.strip('=')
print("'" + ditengah + "'")
dikanan = kanan.strip()
print("'" + dikanan + "'")