import requests
from bs4 import BeautifulSoup
import pymysql.cursors

url="https://news.google.com/news/headlines?hl=tr&gl=TR&ned=tr_tr"
response=requests.get(url)


baglanti = pymysql.connect('localhost','root','','newsdata', autocommit=True,charset='utf8')
connect = baglanti.cursor()



html_iceri=response.content
soup=BeautifulSoup(html_iceri,"html.parser")

linkler=soup.find_all("a",{"class":"nuEeue hzdq5d ME7ew"})
basliklar=soup.find_all("a",{"class":"nuEeue hzdq5d ME7ew"})
kaynaklar=soup.find_all("span",{"class":"IH8C7b Pc0Wt"})
saatler=soup.find_all("span",{"class":"d5kXP YBZVLb"})
keyler=soup.find_all("c-wiz",{"class":"HzT8Gd QGRmIf"})

try:
    with baglanti.cursor() as cursor:
            for link,baslik,kaynak,saat,key in zip(linkler,basliklar,kaynaklar,saatler,keyler):
                url=str(link.get("href").replace("'"," "))
                title=str(baslik.text.replace("'"," "))
                source=str(kaynak.text.replace("'"," "))
                hours=str(saat.text.replace("'"," "))
                anahtar=str(key.text.replace("'"," "))
                sorgu = ("INSERT INTO newsdata (newstitle,newsurl,newsource,newstime,newskey) VALUES (%s,%s,%s,%s,%s)")
                data=title,url,source,hours,anahtar
                cursor.execute(sorgu,data)
    baglanti.commit()

finally:
    baglanti.close()