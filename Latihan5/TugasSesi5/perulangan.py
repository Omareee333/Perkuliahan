print ("Gabriel Omar Prasetyo")
print ("20210801358")
print ("Tugas Sesi 5 Bahasa Pemograman")

print ("Perulangan menggunakan while \n")

jawab = 'Menang'
hitung =  -1

while(True):
    hitung += 1
    jawab = input("Apakah pertandingan hari ini menang ? ") 
    if jawab == 'Kalah':    
        break

print(f"Total Streak Kemenangan: {hitung}")
