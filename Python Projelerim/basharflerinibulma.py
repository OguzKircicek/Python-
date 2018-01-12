bas_harfler = ""

with open("siir.txt","r") as file:
    for satir in file:
        bas_harfler += satir[0]
print(bas_harfler)








