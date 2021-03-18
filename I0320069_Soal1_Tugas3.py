#MUHAMMAD RENGGA SETYA MARLIANNSYAH
#NIM I0320069
#KELAS B

#List nama teman
teman = ['Jefri','Erysa','Efa','Ayu','Memed','Hafiz','Tsania','Akrom','Cita','Ojat']

#Penampilan isi list index 4,6,7
print("list[4,6,7]:",teman[3],",",teman[5],",",teman[6])

#Perubahan isi list index 3,5,9
teman[2]='Nadiya'
teman[4]='Alam'
teman[8]='Iffa'
print("Nama teman baru pada index 3,5,9 :",teman[2],",",teman[4],",",teman[8])

#Penambahan isi list
teman.append('Salma')
teman.append('Raka')
print("Nama teman baru :", teman[10],",",teman[11])

#Penampilan isi list dengan pengulangan
for nama_teman in teman:
    print(nama_teman,"adalah temanku")

#Penampilan panjang list
print("Semua temanku ada {} orang".format(len(teman)))


