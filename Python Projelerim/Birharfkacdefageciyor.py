
kelime="Programlamaodeviveriyapilaridersiuygulamasi"

liste=list(kelime)

kelime_sozluk=dict()

for i in liste:
    if (i in kelime_sozluk):
        kelime_sozluk[i] +=1
    else:
        kelime_sozluk[i]=1

for kelime,sayi in kelime_sozluk.items():
    print("{} kelimeden {} defa geciyor".format(kelime,sayi))

    print("---------------------")


