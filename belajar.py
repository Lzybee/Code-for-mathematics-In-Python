#Python code 

def hitung_kecepatan():
    print("hitung brok")
    jarak = int(input("masukan jarak: "))
    waktu = int(input("masukan waktu: "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan)

def luas_segitiga():
    print("Hitung Brok")
    alas = int(input("masukan alas: "))
    tinggi = int(input("masukan tinggi: "))
    segitiga = 0.5 * (alas * tinggi)
    print("luas Segitiga: ", segitiga)

def luas_balok():
    print("Hitung Brok")
    p = int(input("masukan panjang: "))
    l = int(input("masukan lebar: "))
    t = int(input("masukan tinggi: "))
    balok = (2 * p * l) + (2 * p * t) + (2 * l * t)
    print("luas balok: ", balok)

def luas_bola():
    print("Hitung Brok")
    r = int(input("masukan jari-jari: "))
    bola = 4 * 3.14 * (r ** 2)
    print("luas bola: ", bola)


while True:
    userInput = int(input("\n\npilih rumus yang akan dipakai: \n\n1.Hitung Kecepetan\n2.Luas Segitiga\n3.Luas Balok\n4.Luas Bola\n\n0.Keluar\n\nSilahkan Dipilih: "))
    if(userInput == 1):
        hitung_kecepatan()
    elif(userInput == 2):
        luas_segitiga()
    elif(userInput == 3):
        luas_balok()
    elif(userInput == 4):
        luas_bola()
    else:
        break