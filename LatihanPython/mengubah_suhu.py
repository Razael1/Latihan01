#CELSIUS KE SATUAN LAINNYA

celsius =float(input('suhu celsius = '))

fahrenheit = celsius * 9/5 + 32
print('suhu pada fahrenheit = ',fahrenheit)

reamur = celsius * 4/5
print('suhu pada reamur = ', reamur)

kelvin = celsius + 273
print('suhu pada kelvin = ',kelvin)

#FAHRENHEIT KE SATUAN LAINNYA

fahrenheit =float(input('suhu fahrenheit = '))

celsius = (fahrenheit - 32) * 5/9
print('suhu pada celsius = ',celsius)

reamur = (fahrenheit - 32) * 4/9
print('suhu pada reamur = ', reamur)

kelvin = (fahrenheit - 32) * 5/9 + 273
print('suhu pada kelvin = ',kelvin)

#REAMUR KE SATUAN LAINNYA

reamur =float(input('suhu reamur = '))

celsius = reamur * 5/4
print('suhu pada celsius = ',celsius)

fahrenheit = reamur * 9/4 + 32
print('suhu pada fahrenheit = ', fahrenheit)

kelvin = reamur * 5/4 + 273
print('suhu pada kelvin = ',kelvin)

#KELVIN KE SATUAN LAINNYA

kelvin =float(input('suhu kelvin = '))

celsius = kelvin - 273
print('suhu pada celsius = ',celsius)

fahrenheit = (kelvin - 273) * 9/5 + 32
print('suhu pada fahrenheit = ', fahrenheit)

reamur = (kelvin - 273) * 4/5
print('suhu pada reamur = ',reamur)