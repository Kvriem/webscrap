import requests as r
from bs4 import BeautifulSoup
import pandas as pd

pages=int(input("how many pages you want to scrap"))
bname,price,status=[],[],[]
for i in range(1,pages):
    url=f"https://books.toscrape.com/catalogue/page-{i}.html"
    re=r.get(url)
    html=re.content
    soup=BeautifulSoup(html,"lxml")
    con=soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    
    for i in range(len(con)):
        bname.append(con[i].find("h3").text.strip())
        price.append(con[i].find("p",{"class":"price_color"}).text.strip())
        status.append(con[i].find("p",{"class":"instock availability"}).text.strip())
    

data={'BookName':bname,'Price':price,'Status':status}
df=pd.DataFrame(data)
file_path = r'ENTER UR PATH'
df.to_csv(file_path, index=False)
print("done")
