# Tugas Besar TBFO
# The Sims Simulator
# Rakha Fadhilah 13518097
# David Gozali 13518

import sys
import os


print()
print("        `-:/+++++++++/:-.`                                                                      ")
print("     `:++++++++++++++++++++:                -:::::::                                            ")
print("    -+oooooooooo++ooooooo+:` `........      +ooooooo-     :::::::`        `.-:///++///:-.`      ")
print("   -oooooooo+-.`   `.-/o/`   /oooooooo`    .oooooooo+    .ooooooo+     `:+oooooooooooooooo+:    ")
print("   +oooooooo:                /oooooooo`    +ooooooooo-   +oooooooo.   :ooooooooooooooooooo:`    ")
print("   +sssssssso/-`             /ssssssss.   .ssssssssss+  -sssssssss+  /sssssssso/:::://oo/`      ")
print("   .osssssssssssoo+/-.`      /ssssssss.   :sssssssssss. ossssssssss. ossssssso`        `        ")
print("    `+ssssssssssssssssss+:`  +ssssssss.   osssssssssss+:sssssssssss+ osssssssss+/:.`            ")
print("      `-/oyyyyyyyyyyyyyyyyy/ :yyyyyyyy.  -yyyyyyyyyyyyyyyyyyyyyyyyyy.`oyyyyyyyyyyyyyyo+-`       ")
print("          ///:/osyyyyyyyyyyyo +yyyyyyy.  +yyyyyyyyyyyyyyyyyyyyyyyyyy:  -+yyyyyyyyyyyyyyyy+`     ")
print("                 `.+yyyyyyyyy-.yyyyyyy. `yyyyyyyyyyyyyyyyyyyyyyyyyyyy     .-/+osyyyyyyyyyys`    ")
print("                    yhhhhhhhh-.hhhhhhh. /hhhhhhhsyhhhhhhhhhhyshhhhhhh:          `-ohhhhhhhh-    ")
print("     `+hy+:.`    .:shhhhhhhhy`/hhhhhhh. yhhhhhhh//hhhhhhhhhh/+hhhhhhhs           .+hhhhhhhh-    ")
print("   `/hhhhhhhhhhhhhhhhhhhhhhy.-hhhhhhhh.:hhhhhhhh..hhhhhhhhhh..hhhhhhhhohhhhhhhhhhhhhhhhhhho     ")
print("  `ohhhhhhhhhhhhhhhhhhhhhh+` ohhhhhhhh.shhhhhhhy  shhhhhhhho  yhhhhhhhhhhhhhhhhhhhhhhhhhy/      ")
print("     -/oyhhhhhhhhhhhhys+-    ohhhhhhhh:hhhhhhhh/  -hhhhhhhh.  ohhhhhhhhooyhhhhhhhhhhys+-        ")
print()


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
print("Tuliskan " + "Help" + " untuk memunculkan opsi dari aksi")



def tamat():
    print("TTTTTTTTTTTTTTTTT  AAAAAAAAAAAAAAA      MMMMMMMMMM                 MMMMMMMMMMM      AAAAAAAAAAAAAAAAA  TTTTTTTTTTTTTTTTT   ")
    print("TTTTTTTTTTTTTTTTT AAAAAAAAAAAAAAAAA     MMMMMMMMMMM                MMMMMMMMMMM     AAAAAAAAAAAAAAAAAAA TTTTTTTTTTTTTTTTT   ")
    print("      TTTT       AAAAA        AAAAAA    MMMMM  MMMMM              MMMMMM MMMMM    AAAAAA        AAAAAAA       TTTT          ")
    print("      TTTT      AAAAA          AAAAAA   MMMMM   MMMMM            MMMMMM  MMMMM   AAAAAA          AAAAAAA      TTTT          ")
    print("      TTTT     AAAAAA           AAAAAA  MMMMM    MMMMM          MMMMM    MMMMM  AAAAAAA          AAAAAAAA     TTTT          ")
    print("      TTTT     AAAAAAAAAAAAAAAAAAAAAAA  MMMMM     MMMMM        MMMMM     MMMMM  AAAAAAAAAAAAAAAAAAAAAAAAA     TTTT          ")
    print("      TTTT     AAAAAAAAAAAAAAAAAAAAAAA  MMMMM      MMMMM      MMMMM      MMMMM  AAAAAAAAAAAAAAAAAAAAAAAAA     TTTT          ")
    print("      TTTT     AAAAAA           AAAAAA  MMMMM        MMMMM   MMMMM       MMMMM  AAAAAAA           AAAAAAA     TTTT          ")
    print("      TTTT     AAAAAA           AAAAAA  MMMMM         MMMMM MMMMM        MMMMM  AAAAAAA           AAAAAAA     TTTT          ")
    print("      TTTT     AAAAAA           AAAAAA  MMMMM          MMMMMMMMM         MMMMM  AAAAAAA           AAAAAAA     TTTT          ")
    print("      TTTT     AAAAAA           AAAAAA  MMMMM           MMMMMMM          MMMMM  AAAAAAA           AAAAAAA     TTTT          ")



def tulis():
    print()
    print("Hygiene = " + str(Hygiene))
    print("Energy  = " + str(Energy))
    print("Fun     = " + str(Fun))

def error():
    print("Aksi Tidak Valid")


def start():
    global Hygiene
    global Energy
    global Fun
    global menang
    global kalah

    Hygiene = 0
    Energy = 10
    Fun = 0
    menang = False
    kalah = False

def restart():
    game()

def end():
    global Hygiene
    global Energy
    global Fun
    global menang
    global kalah

    if (((Hygiene== 15) and (Energy==15) and (Fun==15)) ):
        menang = True
    elif ((Hygiene== 0) and (Energy==0) and (Fun==0)):
        kalah = True

def cheat():
    global menang
    Hygiene = 15
    Energy = 15
    Fun = 15 
    menang = True

def dead():
    global kalah 
    Hygiene = 0
    Energy = 0
    Fun = 0
    kalah = True


def isvalid(x,y,z):
    if ((0<=(x)<=15) and (0<=(y)<=15) and (0<=(z)<=15)):
        return True
    else:
        return False



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
    print("                                                          -5 Energy")
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



help()
print("\n")

start()
while(True):
    print("Masukkan Aksi : ", end="")
    aksi = str(input())        

    if (aksi == "Tidur Siang"):
        Hygiene += 0
        Energy += 10
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy -= 10
            Fun -= 0
        
        print("\n")

    elif (aksi == "Tidur Malam"):
        Hygiene += 0
        Energy += 15
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy -= 15
            Fun -= 0
        
        print("\n")

    elif (aksi == "Makan Hamburger"):
        Hygiene += 0
        Energy += 5
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy -= 5
            Fun -= 0
        print("\n")

    elif (aksi == "Makan Pizza"):
        Hygiene += 0
        Energy += 10
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0 
            Energy -= 10
            Fun -= 0
        
        print("\n")

    elif (aksi == "Makan Steak and Beans"):
        Hygiene += 0
        Energy += 15
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy -= 15
            Fun -= 0
        
        print("\n")

    elif (aksi == "Minum Air"):
        Hygiene -= 5 
        Energy += 0
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene += 5 
            Energy -= 0
            Fun -= 0
        
        print("\n")

    elif (aksi == "Minum Kopi"):
        Hygiene -= 10
        Energy += 5
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene += 10
            Energy -= 5
            Fun -= 0
        
        print("\n")
        

    elif (aksi =="Minum Jus"):
        Hygiene -= 5
        Energy += 10
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene += 5
            Energy -= 10 
            Fun -= 0
        
        print("\n")
        

    elif (aksi == "Buang Air Kecil"):
        Hygiene += 5
        Energy += 0
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 5
            Energy -= 0
            Fun -= 0
        
        print("\n")

    elif (aksi == "Buang Air Besar"):
        Hygiene += 10
        Energy -= 5
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 10
            Energy += 5
            Fun -= 0
        
        print("\n")

    elif (aksi == "Bersosialisasi ke Kafe"):
        Hygiene -= 5
        Energy += 10
        Fun += 15
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene += 5
            Energy -= 10
            Fun -= 15
        
        print("\n")

    elif (aksi == "Bermain Media Sosial"):
        Hygiene += 0
        Energy -= 10
        Fun += 10
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy += 10
            Fun -= 10
        
        print("\n")

    elif  (aksi == "Bermain komputer"):
        Hygiene += 0
        Energy -= 10
        Fun += 15
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy += 10
            Fun -= 15
        print("\n")

    elif (aksi == "Mandi"):
        Hygiene += 15
        Energy -= 5
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 15
            Energy += 5
            Fun -= 0
        print("\n")
        

    elif (aksi == ("Cuci Tangan")):
        Hygiene += 5
        Energy += 0
        Fun += 0
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 5
            Energy -= 0
            Fun -= 0
        print("\n")

    elif (aksi == "Mendengarkan Musik di Radio"):
        Hygiene += 0
        Energy -= 5
        Fun += 10
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy += 5
            Fun -= 10
        print("\n")

    elif (aksi == "Membaca Koran"):
        Hygiene += 0
        Energy -= 5
        Fun += 5
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy += 5
            Fun -= 5
        print("\n")

    elif (aksi == "Membaca Novel"):
        Hygiene += 0
        Energy -= 5
        Fun += 10
        if (isvalid(Hygiene,Energy,Fun)):
            tulis()
        else:
            error()
            Hygiene -= 0
            Energy += 5
            Fun -= 10
        print("\n")

    elif (aksi == "Help"):
        help()
    
    elif (aksi == "bajingan"):
        cheat()

    elif (aksi == "matek"):
        dead()

    elif (aksi == "Show"):
        tulis()

    else:
        print("Baca lagi List aksi yang dapat dilakukan atau ketik 'Help' untuk memunculkan list aksi")
        


    end()
    if(menang or kalah):
        break


if (end):

    if(menang):
        print("Selamat Sims Kamu Menang")
        tamat()
    else:
        print("Yah sims kamu mati")
        print("play again?(Y/N)  ",end="")
        play = str(input())
        while((play!='Y') and (play!='N')):
            if (play == 'Y'):
                restart()
            elif(play == 'N'):
                print("Terima kasih sudah bermain di game ini")
                tamat()
                sys.exit()
            else:
                print("mohon ulangi pilihan kamu (Y/N)! ",end="")
                play = str(input())




