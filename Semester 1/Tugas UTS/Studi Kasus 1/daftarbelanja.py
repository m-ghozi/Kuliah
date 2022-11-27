# membuat daftar belanja
# lokasi file

lokasi = "g:/Kuliah/STUDI KASUS 1/"

#menambah daftar belanja
def tambah_belanja(text):
    file = open(lokasi + "belanja.txt", 'a+')
    file.write('\n' + text)

#list belanja 
def daftar_belanja():
    file = open(lokasi + "belanja.txt",'a+')
    file.seek(0)
    text = file.read()
    print(text)

#tentang Apps
def tentang_program():
    tentang = open(lokasi + "program.txt",'r')
    app = tentang.read()
    print(app)

def tentang_saya():
    saya = open(lokasi + "saya.txt",'r')
    apps = saya.read()
    print(apps)

def tanya_pengguna():
    print("Silahkan Masukan keperluan belanja anda ke daftar Belanja")
    print("==================== Daftar Belanja =====================")
    tambah_belanja(input('Mau Belanja Apa : '))
    
loop = True

print('================= Menu ===================')
print('1. Tambah ke Daftar Belanja')
print('2. Daftar Belanja')
print('3. Keluar')
print('4. Tentang Program')
print('5. Tentang Saya')
print('===========================================')
while (loop):
    print('\n')
    menu = input('Masukan menu = ')

    if menu == '1':
        tanya_pengguna()
    elif menu == '2':
        daftar_belanja()
    elif menu == '3':
        quit()
    elif menu == '4':
        tentang_program()
    elif menu == '5':
        tentang_saya()
    else:
        print('Yang diketikan salah')

