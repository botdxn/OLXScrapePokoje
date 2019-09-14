import bs4, requestModule, csv, smtplib

URL = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/'
PRICE_MATCH = 700

def scrapeAll(URL):
    soupParser = bs4.BeautifulSoup(requestModule.requestSite(URL).text, 'html.parser')
    ogloszenia = soupParser.find_all('table', {'summary': 'Ogłoszenie'})
    with open('data.txt', 'a', encoding="UTF-8") as file:
        for ogloszenie in ogloszenia:
            cena = ogloszenie.find('p', {'price'}).text
            cena = cena.replace(" ", "")
            cena = cena.replace("zł", "")
            cena = cena.replace("\t", "").replace("\r", "").replace("\n", "")

            tytul = ogloszenie.find('a', {'data-cy': 'listing-ad-title'}).text
            tytul = str(tytul.replace("\t", "").replace("\r", "").replace("\n", ""))

            link = ogloszenie.find('a', {'marginright5'})['href']
            link = link.replace("\t", "").replace("\r", "").replace("\n", "")

            dataid = ogloszenie['data-id']
            dataid = dataid.replace("\t", "").replace("\r", "").replace("\n", "")

            file.write(tytul+'%'+cena+'%'+link+'%'+dataid+'\n')
        #if int(cena) <= PRICE_MATCH:
            #print(str(tytul), str(cena), str(link), dataid)