
nama = input ("Nama: ")
print(nama)
alamat = input ("alamat: ")
print(alamat)
hobi = input ("hobi: ")
print()

print("nama saya " + nama )
print("saya tinggal di" + alamat)
print("saya memiliki hobi" + hobi)
print("saya dalamm 3 bulan akan belajar python")
print("yuk belajar type data dan matematika")

print('='*25)

operasi = input('Ketik MAU jika ingin tau apa saja type data di python:')
if operasi == 'Mau':
   print('Gaskeun')
elif operasi == 'Moh':
  print('Yawiss rsh')
else : print('Tidak valid')

print('kamu sekarang kuliah')
print("mantap kamu" + nama)
print("Jika kamu" + operasi,"yuk lanjut")

print("hello" + nama)
print("selamat belajr type data di python")

print("1. tipe data integer bilangan bulat")
q = 29
print(type(q))
print()
print("2. tipe dayta float bilangan desimal")
r = 50.75
print(type(r))
print()
print("3. tipe data string karakter dan teks")
s = "dimas"
print(type(s))
print()
print("4. tipe data boolean True or False")
t = False
print(type(t))
print()
print("5. tipe data boolean True or False")
u = complex(5,6)
print(type(u))
print()
print("6. tipe data list")
v = ['apel','pisang','mangga']
print(type(v))
print()
print("7.tipe data tuple")
w = ('mangga','anggur','degan')
print(type(w))
print()
print("8. tipe data range")
x = range(0,6)
print(type(x))
print()
print("9. tipe data dict")
y = {'nama':'dimas','age': 17}
print(type(y))
print()
print("10. tipe data set")
z = {'nama','uwek','age','17'}
print(type(z))
print()
print("11. tipe data frozenset")
a = frozenset({'Angga','Dimas','Otong'})
print(type(a))

print("Yap itu adalah 11 type data di python")
print()
print()
print("Yuk lanjut ke dasar matematika di python")

pertanyaan2 = input ("Ketik MAU jika mau lanjut")
print(pertanyaan2)

print('='*25)

print('Operasi Matematika')
print('  1. Jumlah \t [+]')
print('  2. Kurang \t [-]')
print('  3. Kali \t [*]')
print('  4. Bagi \t [/]')

print()

operasi = input('Pilih operasi (1/2/3/4): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))

print()

if operasi == '1':
  print('kamu memilih penjumlahan')
elif operasi == '2':
  print('kamu memilih pengurangan')
elif operasi == '3':
  print('kamu memilih perkalian')
elif operasi == '4':
  print('kamu memilih pembagian')
else:
  print('Tidak valid')

  print()

if operasi == '1':
    hasil = bilangan_1 + bilangan_2
    print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
    hasil = bilangan_1 - bilangan_2
    print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
     hasil = bilangan_1 * bilangan_2
     print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
    hasil = bilangan_1 / bilangan_2
    print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')

else : print('Tidak valid')
print("TERIMAKASIHH")



