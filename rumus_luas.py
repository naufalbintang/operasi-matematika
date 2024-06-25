'''module luas bangun datar'''

# presegi 
def rumus_luas_persegi() -> int:
    while True:
        try:
            input_sisi: float = float(input('Masukkan panjang: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_sisi

# presegi panjang
def rumus_luas_persegi_panjang() -> int:
    while True:
        try:
            input_panjang: float = float(input('Masukkan panjang: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    while True:
        try:
            input_lebar: float = float(input('Masukkan lebar: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_panjang, input_lebar

# lingkaran
def rumus_luas_lingkaran() -> int:
    while True:
        try:
            input_radius: float = float(input('Masukkan radius: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_radius

# segitiga
def rumus_luas_segitiga() -> int:
    while True:
        try:
            input_alas: float = float(input('Masukkan alas: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    while True:
        try:
            input_tinggi: float = float(input('Masukkan tinggi: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_alas, input_tinggi

# trapesium
def rumus_luas_trapesium() -> int:
    while True:
        try:
            input_atas: float = float(input('Masukkan panjang sisi atas: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    while True:
        try:
            input_bawah: float = float(input('Masukkan panjang sisi bawah: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    while True:
        try:
            input_tinggi: float = float(input('Masukkan tinggi: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_atas, input_bawah, input_tinggi    
        

# jajar genjang
def rumus_luas_jajar_genjang() -> int:
    while True:
        try:
            input_alas: float = float(input('Masukkan panjang alas: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    while True:
        try:
            input_tinggi: float = float(input('Masukkan tinggi: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_alas, input_tinggi
# layang-layang
def rumus_luas_layang_layang() -> int:
    while True:
        try:
            input_d1: float = float(input('Masukkan panjang diagonal 1: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
            continue
    while True:
        try:
            input_d2: float = float(input('Masukkan panjang diagonal 2: '))
            break
        except:
            print('Tolong masukkan bilangan bulat.')
    return input_d1, input_d2