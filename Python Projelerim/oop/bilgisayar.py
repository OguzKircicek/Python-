import random

class Bilgisayar():
    def __init__(self,bil_durum="Kapalı",bil_renk=["beyaz","kırmızı","gri","turuncu"],program="Fifa",renk="Beyaz",bil_prog=["Fifa","Github","Pes","Pycharm"]):
        self.bil_durum=bil_durum
        self.bil_renk=bil_renk
        self.bil_prog=bil_prog
        self.program=program
        self.renk=renk



    def bil_ac(self):
        if(self.bil_durum=="Kapalı"):
            print("Bilgisayar Açılıyor")
            self.bil_durum="Açık"
        else:
            print("Bilgisayar Zaten Açık")
    def bil_kapat(self):
        if (self.bil_durum=="Açık"):
            print("Bilgisayar Kapanıyor")
            self.bil_durum="Kapalı"
        else:
            print("Bilgisayar Zaten Kapalı")
    def bilgi_renk(self):

        rastgele = random.randint(0, len(self.bil_renk) - 1)

        self.renk = self.bil_renk[rastgele]
        print("{} rengi ".format(self.renk))

    def bilgi_prog(self):
        if(self.bil_durum=="Açık"):
            rastgele = random.randint(0, len(self.bil_prog) - 1)

            self.program = self.bil_prog[rastgele]

            print("{} programı açılıyor".format(self.program))
        else:
            print("Bilgisayar Açık Değil Önce onu açınız")


    def __str__(self):
        return "Bilgisayar Durumu : {}\nBilgi Renk: {}\nProgram: {}\n ".format(self.bil_durum,self.bil_renk,self.bil_prog)


bilgisayar=Bilgisayar()

print("""*********Bilgisayar Uygulama******

1.Bilgisayarın Durumu Açmak için

2.Bilgisayar Kapatmak İçin

3.Açık Olan Program

4.Bilgisayar Rengi

5.Bilgisayar Kayıtı


""")

while True:
    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        break
    if (işlem == "1"):
        bilgisayar.bil_ac()
    elif (işlem == "2"):
        bilgisayar.bil_kapat()
    elif (işlem == "3"):
        bilgisayar.bilgi_prog()
    elif (işlem=="4"):
        bilgisayar.bilgi_renk()
    elif (işlem=="5"):
        print(bilgisayar)
    elif (islem=="q"):
        break

    else:
        print("Geçersiz İşlem")

