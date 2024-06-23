'''module luas bangun datar'''

# presegi 
def rumus_luas_persegi() -> float:
    while True:
        input_sisi: float = input('Masukkan panjang sisi: ')
        if input_sisi.isdigit():
            input_sisi: float = float(input_sisi)
            break
        else:
            print('Tolong masukkan angka.')
    return input_sisi ** 2

# presegi panjang
def rumus_luas_persegi_panjang() -> float:
    while True:
        input_panjang: float = input('Masukkan panjang: ')
        if input_panjang.isdigit():
            input_panjang: float = float(input_panjang)
            break
        else:
            print('Tolong masukkan angka.')
    while True:
        input_lebar: float = input('Masukkan lebar: ')
        if input_lebar.isdigit():
            input_lebar: float = float(input_lebar)
            break
        else:
            print('Tolong masukkan angka.')
    return input_panjang * input_lebar

# lingkaran
def rumus_luas_lingkaran() -> float:
    while True:
        input_radius: float = input('Masukkan radius atau jari-jari: ')
        if input_radius.isdigit():
            input_radius: float = float(input_radius)
            break
        else:
            print('Tolong masukkan angka.')
    return 22 / 7 * input_radius ** 2

# segitiga
def rumus_luas_segitiga() -> float:
    while True:
        input_alas: float = input('Masukkan alas: ')
        if input_alas.isdigit():
            input_alas: float = float(input_alas)
            break
        else:
            print('Tolong masukkan angka.') 
    while True:
        input_tinggi: float = input('Masukkan tinggi: ')
        if input_tinggi.isdigit():
            input_tinggi: float = float(input_tinggi)
            break
        else:
            print('Tolong masukkan angka.')
    return input_alas * input_tinggi / 2

# trapesium
def rumus_luas_trapesium() -> float:
    while True:
        input_atas: float = input('Masukkan panjang atas: ')
        if input_atas.isdigit():
            input_atas: float = float(input_atas)
            break
        else:
            print('Tolong masukkan angka.')
    while True:
        input_bawah: float = input('Masukkan panjang bawah: ')
        if input_bawah.isdigit():
            input_bawah: float = float(input_bawah)
            break
        else:
            print('Tolong masukkan angka.')
    while True:
        input_tinggi: float = input('Masukkan tinggi: ')
        if input_tinggi.isdigit():
            input_tinggi: float = float(input_tinggi)
            break
        else:
            print('Tolong masukkan angka.')
    return (input_atas + input_bawah) * input_tinggi / 2    
        

# jajar genjang
def rumus_luas_jajar_genjang() -> float:
    while True:
        input_alas: float = input('Masukkan alas: ')
        if input_alas.isdigit():
            input_alas: float = float(input_alas)
            break
        else:
            print('Tolong masukkan angka.')
    while True:
        input_tinggi: float = input('Masukkan tinggi: ')
        if input_tinggi.isdigit():
            input_tinggi: float = float(input_tinggi)
            break
        else:
            print('Tolong masukkan angka.')
    return input_alas * input_tinggi
# layang-layang
def rumus_luas_layang_layang() -> float:
    while True:
        input_d1: float = input('Masukkan diagonal 1: ')
        if input_d1.isdigit():
            input_d1: float = float(input_d1)
            break
        else:
            print('Tolong masukkan angka.')
    while True:
        input_d2: float = input('Masukkan diagonal 2: ')
        if input_d2.isdigit():
            input_d2: float = float(input_d2)
            break
        else:
            print('Tolong masukkan angka.')
    return input_d1 * input_d2 / 2