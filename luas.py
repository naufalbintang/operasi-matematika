'''module luas bangun datar'''

def luas_persegi() -> float:
    while True:
        input_sisi: float = input('Masukkan panjang sisi: ')
        if input_sisi.isdigit():
            input_sisi: float = float(input_sisi)
            hasil: float = input_sisi ** 2
            break
        else:
            print('Tolong masukkan angka.')
    return hasil