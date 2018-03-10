import requests
from bs4 import BeautifulSoup
import pymysql

url="https://news.google.com/news/headlines?hl=tr&gl=TR&ned=tr_tr"
response=requests.get(url)


baglanti = pymysql.connect('localhost','root','','newsdata', autocommit=True,charset='utf8')
baglanti = baglanti.cursor()



html_iceri=response.content
soup=BeautifulSoup(html_iceri,"html.parser")

linkler=soup.find_all("a",{"class":"nuEeue hzdq5d ME7ew"})
basliklar=soup.find_all("a",{"class":"nuEeue hzdq5d ME7ew"})
kaynaklar=soup.find_all("span",{"class":"IH8C7b Pc0Wt"})
saatler=soup.find_all("span",{"class":"d5kXP YBZVLb"})
keyler=soup.find_all("c-wiz",{"class":"HzT8Gd QGRmIf"})
try:
    with baglanti as cursor:

        for link,baslik,kaynak,saat,key in zip(linkler,basliklar,kaynaklar,saatler,keyler):
            url=link.get("href")
            title=baslik.text
            source=kaynak.text
            hours=saat.text
            anahtar=key.text
            sorgu = "INSERT INTO newsdata ('newstitle','newsurl','newsource','newstime','newskey') VALUES (%%s,%%s,%%s,%%s,%%s)"
            cursor.execute(sorgu,(url,title,source,hours,anahtar))

    cursor.commit()
finally:
    baglanti.close()