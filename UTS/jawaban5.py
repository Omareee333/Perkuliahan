def menu_minuman():
    caps = "Cappucino"
    teh = "Teh"
    print ("Pilihan")
    print ("1.", caps)
    print ("2.", teh)
    print ("3. Keluar")

def nim_nama():
    (input("NIM : ") )
    (input("NAMA : "))

def cappucino():
    caps = "Memilih cappucino"
    print (caps)
    capscaw = int(input("Masukkan harga : "))
    bayar = capscaw + (capscaw * 1 / 10)
    print(bayar)

def teh():
    teh = "Memilih teh"
    print(teh)
    tehh = int(input("Masukkan harga : "))
    bayar = tehh + (tehh * 1 / 10)
    print (bayar)

while True:
    nim_nama()
    menu_minuman()
    pilihan = int(input("masukkan pilihan : "))
    if pilihan == 1:
     cappucino()
    elif pilihan == 2:
        teh()
    elif pilihan == 3:
        break
    else:
        print ("Pilihan salah")
