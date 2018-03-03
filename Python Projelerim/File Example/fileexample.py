gecenler=list()
kalanlar=list()
def not_hesapla(satır):


    satır = satır[:-1]

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"
        gecenler.append(isim+str(son_not)+"\n")
    elif (son_not >= 85):
        harf = "BA"
        gecenler.append(isim +str(son_not)+"\n")
    elif (son_not >= 80):
        harf = "BB"


        gecenler.append(isim +str(son_not)+ "\n")
    elif (son_not >= 75):
        harf = "CB"
        gecenler.append(isim + str(son_not)+"\n")
    elif (son_not >= 70):
        harf = "CC"
        gecenler.append(isim + str(son_not)+"\n")
    elif (son_not >= 65):
        harf = "DC"
        gecenler.append(isim + str(son_not)+"\n")
    elif (son_not >= 60):
        harf = "DD"
        gecenler.append(isim + str(son_not)+"\n")
    elif (son_not >= 55):

        harf = "FD"
        kalanlar.append(isim +str(son_not)+"\n")
    else:
        harf = "FF"
        kalanlar.append(isim + str(son_not)+"\n")

    return isim + "------------------> " + harf + "\n"







with open("C:/ab18/dosya.txt","r",encoding= "utf-8") as file:

    eklenecekler_listesi = []

    for i in file:

        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar.txt","w",encoding="utf-8") as file2:

        for i in eklenecekler_listesi:
            file2.write(i)

    with open("gecenler.txt","w+",encoding="utf-8") as file3:
        for i in gecenler:
            file3.write(i)

    with open("kalanlar.txt","w+",encoding="utf-8") as file4:
        for i in kalanlar:
            file4.write(i)

