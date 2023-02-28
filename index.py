import requests
from bs4 import BeautifulSoup

link = ("https://www.plus500.com/en/")
res = requests.get(link)
soup = BeautifulSoup(res.text, 'lxml')

main = soup.find('span',{"class":"inst-name-wrapper"}).text
print(main)

# <a href="/en/Instruments/CL" title="Oil" dir="ltr">Oil</a>

# //*[@id="inst-details"]/h1

# //*[@id="feedTable"]/div[2]/table/tbody/tr[1]/th/span/a

# //*[@id="feedTable"]/div[2]/table/tbody/tr[1]/th/span
# <span class="inst-name-wrapper"><a href="/en/Instruments/CL" title="Oil" dir="ltr">Oil</a> <!----></span>