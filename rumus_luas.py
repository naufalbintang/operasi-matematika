'''module luas bangun datar'''

# presegi 
def rumus_luas_persegi() -> int:
    while True:
        input_sisi: int = input('Masukkan panjang: ')
        try:
            input_sisi: int = int(input_sisi)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_sisi

# presegi panjang
def rumus_luas_persegi_panjang() -> int:
    while True:
        input_panjang: int = input('Masukkan panjang: ')
        try:
            input_panjang: int = int(input_panjang)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        input_lebar: int = input('Masukkan lebar: ')
        try:
            input_lebar: int = int(input_lebar)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_panjang, input_lebar

# lingkaran
def rumus_luas_lingkaran() -> int:
    while True:
        input_radius: int = input('Masukkan radius: ')
        try:
            input_radius: int = int(input_radius)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_radius

# segitiga
def rumus_luas_segitiga() -> int:
    while True:
        input_alas: int = input('Masukkan alas: ')
        try:
            input_alas: int = int(input_alas)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        input_tinggi: int = input('Masukkan tinggi: ')
        try:
            input_tinggi: int = int(input_tinggi)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_alas, input_tinggi

# trapesium
def rumus_luas_trapesium() -> int:
    while True:
        input_atas: int = input('Masukkan panjang sisi atas: ')
        try:
            input_atas: int = int(input_atas)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        input_bawah: int = input('Masukkan panjang sisi bawah: ')
        try:
            input_bawah: int = int(input_bawah)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        input_tinggi: int = input('Masukkan tinggi: ')
        try:
            input_tinggi: int = int(input_tinggi)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_atas, input_bawah, input_tinggi    
        

# jajar genjang
def rumus_luas_jajar_genjang() -> int:
    while True:
        input_alas: int = input('Masukkan panjang alas: ')
        try:
            input_alas: int = int(input_alas)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        input_tinggi: int = input('Masukkan tinggi: ')
        try:
            input_tinggi: int = int(input_tinggi)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_alas, input_tinggi
# layang-layang
def rumus_luas_layang_layang() -> int:
    while True:
        input_d1: int = input('Masukkan panjang diagonal 1: ')
        try:
            input_d1: int = int(input_d1)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        input_d2: int = input('Masukkan panjang diagonal 2: ')
        try:
            input_d2: int = int(input_d2)
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    return input_d1, input_d2