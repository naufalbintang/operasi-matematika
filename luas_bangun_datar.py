'''module luas bangun datar'''

# presegi 
def persegi() -> float:
    while True:
        try:
            input_sisi: float = float(input('Masukkan panjang: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_sisi

# presegi panjang
def persegi_panjang() -> float:
    while True:
        try:
            input_panjang: float = float(input('Masukkan panjang: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            input_lebar: float = float(input('Masukkan lebar: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_panjang, input_lebar

# lingkaran
def lingkaran() -> float:
    while True:
        try:
            input_radius: float = float(input('Masukkan radius: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_radius

# segitiga
def segitiga() -> float:
    while True:
        try:
            input_alas: float = float(input('Masukkan alas: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            input_tinggi: float = float(input('Masukkan tinggi: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_alas, input_tinggi

# trapesium
def trapesium() -> float:
    while True:
        try:
            input_atas: float = float(input('Masukkan panjang sisi atas: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            input_bawah: float = float(input('Masukkan panjang sisi bawah: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            input_tinggi: float = float(input('Masukkan tinggi: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_atas, input_bawah, input_tinggi    
        

# jajar genjang
def jajar_genjang() -> float:
    while True:
        try:
            input_alas: float = float(input('Masukkan panjang alas: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            input_tinggi: float = float(input('Masukkan tinggi: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_alas, input_tinggi
# layang-layang
def layang_layang() -> float:
    while True:
        try:
            input_d1: float = float(input('Masukkan panjang diagonal 1: '))
            break
        except:
            print('Tolong masukkan bilangan.')
            continue
    while True:
        try:
            input_d2: float = float(input('Masukkan panjang diagonal 2: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return input_d1, input_d2