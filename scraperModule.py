import bs4, requestModule
from selenium import webdriver
from re import sub
from decimal import Decimal

URL = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/'


def scrapeAll(URL):
    soupParser = bs4.BeautifulSoup(requestModule.requestSite(URL).text, 'html.parser')
    ogloszenia = soupParser.find_all('table', {'summary': 'Ogłoszenie'})

    for ogloszenie in ogloszenia:
        cena = ogloszenie.find('p', {'price'}).text
        cena = cena.replace(" ", "")
        cena = cena.replace("zł", "")

        tytul = ogloszenie.find('a', {'data-cy': 'listing-ad-title'})

        link = ogloszenie.find('a', {'marginright5'})['href']

        dataid = ogloszenie['data-id']

        if int(cena) <= 800:
            print(str(tytul.text), str(cena), str(link), dataid)
            
scrapeAll(URL)