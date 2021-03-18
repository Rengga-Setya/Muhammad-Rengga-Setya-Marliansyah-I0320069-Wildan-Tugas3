#MUHAMMAD RENGGA SETYA MARLIANNSYAH
#NIM I0320069
#KELAS B

#Biodata
bio={'Nama':'Rengga',
     'Hobi 1':'Berenang','Hobi 2':'Lari','Hobi 3':'Menonton anime',
     'Instagram': 'rengga.sm','Whatsapp':'089608679776','Line':'mr.zack21',
     'Lagu favorit 1':'Yellow','Lagu favorit 2':'One only','Lagu favorit 3':'Live forever',
     'Makanan favorit  1':'Gado-gado','Makanan favorit 2':'Mie ayam','Makanan favorit 3':'Tempe bacem'}
print("Biodata:",bio)

#Perubahan salah satu hobi dan sosial media
bio['Hobi 3']='Mendengarkan lagu'
bio['Line']='m.rengga_21'

#Pengapusan 2 Makanan kesukaan
del bio['Makanan favorit 2']
del bio['Makanan favorit 3']

#Penambahan hobi
bio['Hobi 4']='Bermain drum'

print("Biodata setelah diubah:",bio)