def weton(tanggal, bulan, tahun):
    """Menentukan weton berdasarkan tanggal, bulan, dan tahun.

    Args:
        tanggal: Tanggal lahir (int).
        bulan: Bulan lahir (int).
        tahun: Tahun lahir (int).

    Returns:
        String yang menyatakan weton.
    """

    '''# pasaran
    pasaran = ["legi", "pahing", "pon", "wage", "kliwon"]
    # neptu
    nama_hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    neptu_hari = [5, 4, 3, 7, 8, 6, 9]

    #Hitung jumlah hari dari tahun 1 hingga tahun input
    jumlah_hari = 0

    # Perhitungan jumlah hari
    for i in range(1, tahun):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            jumlah_hari += 366
        else:
            jumlah_hari += 365

    # Perhitungan jumlah hari dari bulan Januari sampai bulan input
    for i in range(1, bulan):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            jumlah_hari += 31
        elif i == 2:
            if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
                jumlah_hari += 29
            else:
                jumlah_hari += 28
        else:
            jumlah_hari += 30

    # Jumlahkan tanggal
    jumlah_hari += tanggal

    # Tentukan hari dan pasaran
    hari_index = jumlah_hari % 7  # Indeks untuk hari
    pasaran_index = jumlah_hari % 5 # Indeks untuk pasaran

    return f"{nama_hari[hari_index]} {pasaran[pasaran_index]}"

# Contoh penggunaan
tanggal = int(input("Masukkan tanggal lahir: "))
bulan = int(input("Masukkan bulan lahir: "))
tahun = int(input("Masukkan tahun lahir: "))

weton_lahir = weton(tanggal, bulan, tahun)
print(f"Weton: {weton_lahir}")'''


def weton(tanggal, bulan, tahun):
    """Menentukan weton berdasarkan tanggal, bulan, dan tahun.

    Args:
        tanggal: Tanggal lahir (int).
        bulan: Bulan lahir (int).
        tahun: Tahun lahir (int).

    Returns:
        String yang menyatakan weton.
    """
    # Pasaran dan hari dalam kalender Jawa
    pasaran = ["Legi", "Pahing", "Pon", "Wage", "Kliwon"]
    nama_hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

    # Jumlah hari dalam setiap bulan
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Hitung total jumlah hari dari tahun 1 sampai tahun input
    jumlah_hari = 0

    # Tambahkan hari dari tahun-tahun penuh sebelum tahun input
    for tahun_sekarang in range(1, tahun):
        if (tahun_sekarang % 4 == 0 and tahun_sekarang % 100 != 0) or (tahun_sekarang % 400 == 0):
            jumlah_hari += 366  # Tahun kabisat
        else:
            jumlah_hari += 365  # Tahun biasa

    # Tambahkan hari dari bulan-bulan sebelum bulan input
    for bulan_sekarang in range(1, bulan):
        if bulan_sekarang == 2 and ((tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)):
            jumlah_hari += 29  # Februari tahun kabisat
        else:
            jumlah_hari += hari_per_bulan[bulan_sekarang - 1]

    # Tambahkan hari dari tanggal input
    jumlah_hari += tanggal

    # Tentukan hari dan pasaran berdasarkan indeks
    hari_index = jumlah_hari % 7  # Indeks hari (0 untuk Minggu, dst.)
    pasaran_index = jumlah_hari % 5  # Indeks pasaran (0 untuk Legi, dst.)

    # Gabungkan nama hari dan pasaran
    return f"{nama_hari[hari_index]} {pasaran[pasaran_index]}"

# Contoh penggunaan
tanggal = int(input("Masukkan tanggal lahir: "))
bulan = int(input("Masukkan bulan lahir: "))
tahun = int(input("Masukkan tahun lahir: "))

weton_lahir = weton(tanggal, bulan, tahun)
print(f"Weton: {weton_lahir}")
