import os
import luas_bangun_datar
import keliling_bangun_datar

def fungsi_input_pilih_operasi() -> int:
    while True:
        input_operasi: int = input('\nMasukkan pilihan: ')
        print(' ')
        if input_operasi.isdigit():
            input_operasi = int(input_operasi)
            if 1 <= input_operasi <= len(pilihan_operasi):
                break
            else:
                print(f'Masukkan angka antara 1 - {len(pilihan_operasi)}.')
        else:
            print('Tolong masukkan angka.')
    return input_operasi

def fungsi_input_pilih_luas() -> int:
    while True:
        input_luas: int = input('\nMasukkan pilihan luas: ')
        if input_luas.isdigit():
            input_luas: int = int(input_luas)
            if 1 <= input_luas <= len(pilihan_luas):
                break
            else:
                print(f'Masukkan angka antara 1 - {len(pilihan_luas)}.')        
        else:
            print('Tolong masukkan angka.')
    return input_luas

def fungsi_input_pilih_keliling() -> int:
    while True:
        input_keliling: int = input('\nMasukkan pilihan keliling: ')
        if input_keliling.isdigit():
            input_keliling: int = int(input_keliling)
            if 1 <= input_keliling <= len(pilihan_keliling):
                break
            else:
                print(f'Masukkan angka antara 1 - {len(pilihan_keliling)}')
        else:
            print('Tolong masukkan angka.')
    return input_keliling
    
'''MAIN PROGRAM'''
while True:
    os.system('cls')
    pilihan_operasi: list[str] = [
        'Keluar',
        'Luas',
        'Keliling'
    ]
    
    pilihan_luas: list[str] = [
        'Keluar',
        'Luas Persegi',
        'Luas Persegi Panjang',
        'Luas Lingkaran',
        'Luas Segitiga',
        'Luas Trapesium',
        'Luas Jajar Genjang',
        'Luas Layang - Layang',
    ]
    
    pilihan_keliling: list[str] = [
        'Keluar',
        'Keliling Persegi',
        'Keliling Persegi Panjang',
        'Keliling Lingkaran',
        'Keliling Segitiga',
        'Keliling Trapesium',
        'Keliling Jajar Genjang',
        'Keliling Layang - Layang',
    ]

    print(f'\n{'OPERASI MATEMATIKA':=^50}\n')
    for nomor, operasi in enumerate(pilihan_operasi, 1):
        print(f'{nomor}. {operasi}')
        
    # input operasi
    input_operasi: int = fungsi_input_pilih_operasi()
    
    # 1. keluar
    if input_operasi == 1:
        break
    
    # 2. Luas
    elif input_operasi == 2:
        for nomor, luas in enumerate(pilihan_luas, 1):
            print(f'{nomor}. {luas}') 
        
        # input luas
        input_luas: int = fungsi_input_pilih_luas()
        
        # keluar
        if input_luas == 1:
            break
        
        # luas persegi
        elif input_luas == 2:
            sisi: int = luas_bangun_datar.persegi()
            luas_persegi: int = sisi ** 2
            print(f'{sisi} x {sisi} = {luas_persegi:.2f}')
            
        # luas persegi panjang
        elif input_luas == 3:
            panjang: int
            lebar: int
            panjang, lebar = luas_bangun_datar.persegi_panjang()
            luas_persegi_panjang: float = panjang * lebar
            print(f'{panjang} x {lebar} = {luas_persegi_panjang:.2f}')

        # luas lingkaran
        elif input_luas == 4:
            radius: int = luas_bangun_datar.lingkaran()
            luas_lingkaran = 22 / 7 * radius ** 2
            print(f'22 / 7 x {radius} x {radius} = {luas_lingkaran:.2f}')
                
            
        # luas segitiga
        elif input_luas == 5:
            alas: int
            tinggi: int
            alas, tinggi = luas_bangun_datar.segitiga()
            luas_segitiga: float = alas * tinggi / 2
            print(f'{alas} x {tinggi} / 2 = {luas_segitiga:.2f}')
            
        # luas trapesium
        elif input_luas == 6:
            atas: int
            bawah: int
            tinggi: int
            atas, bawah, tinggi = luas_bangun_datar.trapesium()
            luas_trapesium: float = (atas + bawah) * tinggi / 2
            print(f'({atas} + {bawah}) x {tinggi} / 2 = {luas_trapesium:.2f}')
            
        # luas jajar genjang
        elif input_luas == 7:
            alas: int
            tinggi: int
            alas, tinggi = luas_bangun_datar.jajar_genjang()
            luas_jajar_genjang: int = alas * tinggi
            print(f'{alas} x {tinggi} = {luas_jajar_genjang:.2f}')
        
        # luas layang-layang
        elif input_luas == 8:
            d1: int
            d2: int
            d1, d2 = luas_bangun_datar.layang_layang()
            luas_layang_layang: float = d1 * d2 / 2 
            print(f'{d1} x {d2} / 2 = {luas_layang_layang:.2f}')
        else:
            print('Maaf operasi tidak tersedia.')
            break
    
    # 3. keliling
    elif input_operasi == 3:
        for nomor, operasi in enumerate(pilihan_keliling, 1):
            print(f'{nomor}. {operasi}')
            
        # input keliling
        input_keliling: int = fungsi_input_pilih_keliling()
    
        # keluar
        if input_keliling == 1:
            break
        
        # keliling persegi
        if input_keliling == 2:
            sisi: float = keliling_bangun_datar.persegi()
            keliling_persegi: float = sisi * 4
            print(f'{sisi} x 4 = {keliling_persegi:.2f}')
        
        # keliling persegi panjang
        elif input_keliling == 3:
            panjang: int
            lebar: int
            panjang, lebar = keliling_bangun_datar.persegi_panjang()
            keliling_persegi_panjang: float = (panjang + lebar) * 2
            print(f'({panjang} + {lebar}) x 2 = {keliling_persegi_panjang:.2f}')
            
        # keliling lingkaran
        elif input_keliling == 4:
            radius: float = keliling_bangun_datar.lingkaran()
            keliling_lingkaran: float = 2 * 22 / 7 * radius
            print(f'2 * 22 / 7 * {radius} = {keliling_lingkaran:.2f}')
            
        # keliling segitiga
        elif input_keliling == 5:
            sisi_1: float
            sisi_2: float
            sisi_3: float
            sisi_1, sisi_2, sisi_3 = keliling_bangun_datar.segitiga()
            keliling_segitiga: float = sisi_1 + sisi_2 + sisi_3
            print(f'{sisi_1} + {sisi_2} + {sisi_3} = {keliling_segitiga}')
        
        # keliling trapesium
        elif input_keliling == 6:
            sisi_1: float
            sisi_2: float
            sisi_3: float
            sisi_4: float
            sisi_1, sisi_2, sisi_3, sisi_4 = keliling_bangun_datar.trapesium()
            keliling_trapesium: float = sisi_1 + sisi_2 + sisi_3 + sisi_4
            print(f'{sisi_1} + {sisi_2} + {sisi_3} + {sisi_4} = {keliling_trapesium}')
                
        
        # keliling jajar genjang
        elif input_keliling == 7:
            sisi_1: float
            sisi_2: float
            sisi_1, sisi_2 = keliling_bangun_datar.jajar_genjang()
            keliling_jajar_genjang: float = (sisi_1 + sisi_2) * 2
            print(f'({sisi_1} + {sisi_2}) x 2  =  {keliling_jajar_genjang}')
        
        # keliling layang-layang
        elif input_keliling == 8:
            sisi_1: float
            sisi_2: float
            sisi_1, sisi_2 = keliling_bangun_datar.layang_layang()
            keliling_layang_layang: float = (sisi_1 + sisi_2) * 2
            print(f'({sisi_1} + {sisi_2}) x 2  =  {keliling_layang_layang}')
        
    else:
        print('Maaf operasi tidak tersedia.')  



    # break
    is_done: str = str(input('Apakah sudah selesai (y/n)? '))
    if is_done.lower() == 'y':
        break
    elif is_done.lower() == 'n':
        None
    else:
        print('Invalid input, exiting program.')
        break
    