'''module keliling bangun datar'''

def persegi() -> float:
    while True:
        try:
            sisi: float = float(input('Masukkan panjang sisi: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return sisi        

def persegi_panjang() -> float:
    while True:
        try:
            panjang: float = float(input('Masukkan panjang: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            lebar: float = float(input('Masukkan lebar: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return panjang, lebar

def lingkaran() -> float:
    while True:
        try:
            radius: float = float(input('Masukkan radius: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return radius

def segitiga() -> float:
    while True:
        try:
            sisi_1: float = float(input('Masukkan panjang sisi 1: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_2: float = float(input('Masukkan panjang sisi 2: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_3: float = float(input('Masukkan sisi 3: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return sisi_1, sisi_2, sisi_3

def trapesium() -> float:
    while True:
        try:
            sisi_1: float = float(input('Masukkan panjang sisi 1: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_2: float = float(input('Masukkan panjang sisi 2: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_3: float = float(input('Masukkan panjang sisi 3: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_4: float = float(input('Masukkan panjang sisi 4: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return sisi_1, sisi_2, sisi_3, sisi_4

def jajar_genjang() -> float:
    while True:
        try:
            sisi_1: float = float(input('Masukkan panjang sisi 1: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_2: float = float(input('Masukkan panjang sisi 2: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return sisi_1, sisi_2

def layang_layang() -> float:
    while True:
        try:
            sisi_1: float = float(input('Masukkan panjang sisi 1: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    while True:
        try:
            sisi_2: float = float(input('Masukkan panjang sisi 2: '))
            break
        except:
            print('Tolong masukkan bilangan.')
    return sisi_1, sisi_2
    
    
    
    