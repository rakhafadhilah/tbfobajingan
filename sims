# Tugas Besar TBFO
# The Sims Simulator
# Rakha Fadhilah 13518097
# David Gozali 13518

def cek():
    if ((0<=(Hygiene+Hygiene1)<=15) and (0<=(Energy+Energy1)<=15) and (0<=(Fun+Fun1)<=15)):

        print ("Hygiene = " + str(Hygiene+Hygiene1))
        print ("Energy = " + str(Energy+Energy1))
        print ("Fun = " + str(Fun+Fun1))
        Hygiene2 = Hygiene+Hygiene1
        Energy2 = Energy+Energy1
        Fun2 = Fun+Fun1

    else:
        Hygiene2 = Hygiene
        Energy2 = Energy
        Fun2 = Fun
        print ("Aksi Tidak Valid")
        print ("Hygiene = " + str(Hygiene2))
        print ("Energy = " + str(Energy2))
        print ("Fun = " +str(Fun2))

def selesai():
    if(((Hygiene!= 15) and (Energy!=15) and (Fun!=15)) or ((Hygiene!= 0) and (Energy!=0) and (Fun!=0))):
        end = False
    else:
        end = True

def help():
    print(" 1. Tidur Siang                                      2.Tidur Malam")
    print("     +10 Energy                                         +15 Energy")
    print(" 3. Makan Hamburger                                  4. Makan Pizza")
    print("     +5 Energy                                           +10 Energy")   
    print(" 5. Steak and Beans")
    print("     +15 Energy")
    print(" 6. Minum Air                                        7. Minum Kopi ")
    print("     -5 Hygiene                                          +5 Energy")
    print("                                                         -10 Hygiene")
    print(" 8. Minum Jus")
    print("     +10 Energy")
    print("     -5 Hygiene")
    print(" 9. Buang Air Kecil                                  10. Buang Air Besar")
    print("     +5 Hygiene                                           +10 Hygiene")
    print("                                                          -5 Enegery")
    print(" 11. Bersosialisasi ke Kafe                          12. Bermain Media Sosial")
    print("     +15 Fun                                              +10 Fun")
    print("     -10 Energy                                           -10 Energy")
    print("     -5 Hygiene")
    print(" 13. Bermain komputer                                14. Mendengarkan Musik di Radio")
    print("     +15 Fun                                              +10 Fun")
    print("     -10 Energy                                           -5 Energy")
    print(" 15. Mandi                                           16. Cuci Tangan")
    print("     +15 Hygiene                                          +5 Hygiene")
    print("     -5 Energy")
    print(" 17. Membaca Koran                                   18. Membaca Novel")
    print("     +5 Fun                                               +10 Fun")
    print("     -5 Energy                                            -5 Energy")



print("The Sims merupakan permainan yang dibuat oleh Maxis dan didistribusikan oleh Electronic Arts. ")
print("The Sims memberikan sebuah pengalaman untuk mengatur setiap karakter dalam sebuah kota untuk membangun kota tersebut.")
print("Permainan akan dilakukan secara real time dan mengharuskan pemainnya untuk benar-benar memperhatikan setiap karakter dalam kota tersebut, dan bisa memilih goal-goal yang ingin dicapai.")
print("Setiap pemain akan mengatur kegiatan seseorang dalam satu hari.")
print("emain dapat memilih satu diantara banyak aksi yang dapat dilakukan, dimana tiap aksi yang dipilih memiliki konsekuensi baik positif maupun negatif.")
print("Seperti layaknya manusia, aktor pada The Sims dapat mengalami perubahan kondisi, seperti lapar, bosan, lelah, dan lainnya.")
print("Kondisi-kondisi tersebut digambarkan menjadi beberapa atribut.")
print("Terdapat beberapa atribut dalam permainan The Sims yang dapat mempengaruhi keberjalanan permainan.")
print("Atribut tersebut adalah sebagai berikut.")
print("     1. Hygiene, merupakan tingkat kebersihan dari pemain")
print("     2. Bladder, merupakan tingkat keinginan pemain untuk membuang air besar atau air kecil.")
print("     3. Hunger, merupakan tingkat kelaparan pemain.")
print("     4. Energy, merupakan tingkat energi yang dimiliki pemain.")
print("     5. Social, merupakan tingkat kesosialan yang dimiliki pemain.")
print("     6. Fun, merupakan tingkat kesenangan dari pemain.")
print("Untuk mempermudah tugas besar ini, atribut-atribut tersebut dimodifikasi sebagai berikut:")
print("     1. Hygiene, gabungan dari atribut Hygiene dan Bladder dalam The Sims.")
print("     2. Energy, gabungan dari atribut Energy dan Hunger dalam The Sims.")
print("     3. Fun, gabungan dari atribut Fun dan Social dalam The Sims.\n")
print("Setiap atribut memiliki nilai maksimum 15 dan nilai minimum 0.")
print("Kondisi awal pemain selalu dalam keadaan sudah bangun tidur dengan atribut Hygiene bernilai 0, Energy bernilai 10, dan Fun bernilai 0.")
print("Permainan dinyatakan selesai jika semua atribut bernilai 0 atau semua atribut bernilai 15.\n")
print("Berikut ini adalah tabel aksi yang dapat dilakukan, rentang waktu untuk melakukan aksi tersebut, dan konsekuensinya:")
print("\n\n")
print("Tuliskan " + "Help" + "untuk memunculkan opsi dari aksi")

help()
print("\n")

while(selesai == False):

    Hygiene = 0
    Energy = 10
    Fun = 0


    while (((Hygiene<=15) and (Energy<=15) and (Fun<=15)) or ((Hygiene>=0) and (Energy>=0) and (Fun>=0))):
        print("Masukkan Aksi : ")
        aksi = str(input())
        if (aksi == "Tidur Siang"):
            Hygiene1 = 0
            Energy1 = 10
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Tidur Malam"):
            Hygiene1 = 0
            Energy1 = 15
            Fun = 0
            cek()
            print("\n")

        if (aksi == "Makan Hamburger"):
            Hygiene1 = 0
            Energy1 = 5
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Makan Pizza"):
            Hygiene1 = 0
            Energy1 = 10
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Makan Steak and Beans"):
            Hygiene1 = 0
            Energy1 = 15
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Minum Air"):
            Hygiene1 = 5 *(-1)
            Energy1 = 0
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Minum Kopi"):
            Hygiene1 = 10*(-1)
            Energy1 = 5
            Fun1 = 0
            cek()
            print("\n")
            

        if (aksi =="Minum Jus"):
            Hygiene1 = 5*(-1)
            Energy1 = 10
            Fun1 = 0
            cek()
            print("\n")
            

        if (aksi == "Buang Air Kecil"):
            Hygiene1 = 5
            Energy1 = 0
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Buang Air Besar"):
            Hygiene1 = 10
            Energy1 = 5*(-1)
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Bersosialisasi ke Kafe"):
            Hygiene1 = 5*(-1)
            Energy1 = 10
            Fun1 = 15
            cek()
            print("\n")

        if (aksi == "Bermain Media Sosial"):
            Hygiene1 = 0
            Energy1 = 10*(-1)
            Fun1 = 10
            cek()
            print("\n")

        if  (aksi == "Bermain Komputer"):
            Hygiene1 = 0
            Energy1 = 10*(-1)
            Fun1 = 15
            cek()
            print("\n")

        if (aksi == "Mandi"):
            Hygiene1 = 15
            Energy1 = 5*(-1) 
            Fun1 = 0
            cek()
            print("\n")
            

        if (aksi == ("Cuci Tangan")):
            Hygiene1 = 5
            Energy1 = 0
            Fun1 = 0
            cek()
            print("\n")

        if (aksi == "Mendengarkan Musik di Radio"):
            Hygiene1 = 0
            Energy1 = 5*(-1)
            Fun1 = 10
            cek()
            print("\n")

        if (aksi == "Membaca Koran"):
            Hygiene1 = 0
            Energy1 = 5*(-1)
            Fun1 = 5
            cek()
            print("\n")

        if (aksi == "Membaca Novel"):
            Hygiene1 = 0
            Energy1 = 5*(-1)
            Fun1 = 10
            cek()
            print("\n")

        if (aksi == "Help"):
            help()
            
#        if (((Hygiene>15) and (Energy>15) and (Fun>15)) or ((Hygiene<0) and (Energy<0) and (Fun<0))):
#            print ("Aksi Tidak valid")
#            Hygiene1 = Hygiene 
#            Energy1 = Energy
#            Fun1 = Fun
#            print ("Aksi Tidak valid")
#           print (Hygiene1)
#           print (Energy1)
#            print (Fun1)

#        if (((Hygiene<=15) and (Energy<=15) and (Fun<=15)) or ((Hygiene>=0) and (Energy>=0) and (Fun>=0))):

#            print ("Aksi valid")
#
#            print (Hygiene)
#            print (Energy)
#            print (Fun)


            
        
#    print ("Hygiene = " + Hygiene)
#    print ("Energy = " + Energy)
#    print ("Fun = " + Fun)
            

