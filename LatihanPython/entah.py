x =int(input('masukkan angka = '))
salah = x < 3 or x > 10
benar = x > 3 and x <  10
print("lebih dari 3 dan kurang dari 10 = ",benar)
print("kurang dari 3 atau lebih dari 10 = ",salah)


x =int(input('masukkan angka = '))
benar = x > 0 and x < 5
entah = x > 8 and x < 11
print(benar or entah)

benar = x < 0
entah = x > 5 and x < 8
ynt = x > 11
print(benar or entah  or ynt)

x = float(input("\nMasukkan angka: "))
y = 0 < x < 5 or 8 < x < 11
print("Status angka: ",y)

y = x < 0 or 5 < x < 8 or x > 11
print("Status angka: ",y)



