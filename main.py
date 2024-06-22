import os
from rumus_luas import rumus_luas_persegi
from rumus_luas import rumus_luas_persegi_panjang
from rumus_luas import rumus_luas_lingkaran
from rumus_luas import rumus_luas_segitiga
from rumus_luas import rumus_luas_trapesium


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
            input_luas: float = int(input_luas)
            if 1 <= input_luas <= len(pilihan_luas):
                break
            else:
                print(f'Masukkan angka antara 1 - {len(pilihan_luas)}.')        
        else:
            print('Tolong masukkan angka.')
    return input_luas

def fungsi_input_luas_persegi() -> float:
    while True:
        input_luas_persegi: float = input('Masukkan panjang sisi: ')
        print(' ')
        if input_luas_persegi.isdigit():
            input_luas_persegi: float = float(input_luas_persegi)
            if 1 <= input_luas_persegi <= len(pilihan_luas):
                break
            else:
                print(f'Masukkan angka antara 1 - {len(pilihan_luas)}')
        else:
            print('Tolong masukkan angka.')
    
    return input_luas_persegi

    
'''MAIN PROGRAM'''
while True:
    os.system('cls')
    pilihan_operasi: list[str] = [
        'Keluar',
        'Luas',
        'Keliling'
    ]
    
    pilihan_luas: list[str] = [
        'Luas Persegi',
        'Luas Persegi Panjang',
        'Luas Lingkaran',
        'Luas Segitiga',
        'Luas Trapesium',
        'Luas Jajar Genjang',
        'Luas Layang - Layang',
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
        
        # luas persegi
        if input_luas == 1:
            luas_persegi: float = rumus_luas_persegi()
            print(f'Hasil luas persegi = {luas_persegi:.2f}')
            
        # luas persegi panjang
        elif input_luas == 2:
            luas_persegi_panjang: float = rumus_luas_persegi_panjang()
            print(f'Hasil luas persegi panjang = {luas_persegi_panjang:.2f}')

        # luas lingkaran
        elif input_luas == 3:
            luas_lingkaran: float = rumus_luas_lingkaran()
            print(f'Hasil luas lingkaran = {luas_lingkaran:.2f}')
        
        # luas segitiga
        elif input_luas == 4:
            luas_segitiga: float = rumus_luas_segitiga()
            print(f'Hasil luas segitiga = {luas_segitiga}')
            
        # luas trapesium
        elif input_luas == 5:
            luas_trapesium: float = rumus_luas_trapesium()
            print(f'Hasil luas trapesium = {luas_trapesium}')
        
        else:
            print('Maaf operasi tidak tersedia.')
            break
        



    # break
    is_done: str = str(input('Apakah sudah selesai (y/n)? '))
    if is_done.lower() == 'y':
        break
    elif is_done.lower() == 'n':
        None
    else:
        print('Invalid input, exiting program.')
        break