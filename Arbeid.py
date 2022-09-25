import requests
from bs4 import BeautifulSoup
import pandas as pd

def hentdata(side):
    print(side,"Er i hentdata")
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    url = f'https://www.finn.no/job/fulltime/search.html?job_duration=1816&location=0.20001&3'
    r =requests.get(url,headers)
#    return r.status_code
    soup = BeautifulSoup(r.content,"lxml")
#    print(soup,'Er i hent data')
    return soup

def omformdata(soup):
    print('ER i omform')
    divs = soup.find_all('div', class_ = 'ads__unit__content__keys')
    divs2 = soup.find_all('div', class_ = 'ads__unit__content__list')
    antall = len(divs2)
#    print(antall,"antall Stillinger 2")
#    tittel = []
    for i in range(len(divs)):
       print(divs[i].text,"innhold divs1")
       print(divs2[i].text,"innhold divs2")
       firma = divs2[i].text.strip()
       
       antall = divs[i].text.strip()
#       tittel.append(utdata)
       jobber ={
           'firma' : firma,
           'antall stillinger': antall
       }
       tittel.append(jobber)
    return

tittel = []
for i in range(0,10,50):
    print(f'Henter side Gunnar,{i}')
    c = hentdata(i)
    omformdata(c)
print(len(tittel))

df = pd.DataFrame(tittel)
print(df.head())
df.to_csv('Arbeid.txt')
