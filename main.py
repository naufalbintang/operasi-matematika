import os
import luas

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
        print(' ')
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
            luas.luas_persegi()
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