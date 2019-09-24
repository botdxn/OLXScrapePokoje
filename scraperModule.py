import bs4, requestModule

def scrapeAll():
    soupParser = bs4.BeautifulSoup(requestModule.requestSites().text, 'html.parser')
    ogloszenia = soupParser.find_all('table', {'summary': 'Ogłoszenie'})

    with open('data.txt', 'w+', encoding="UTF-8") as file:
        for ogloszenie in ogloszenia:
            cena = ogloszenie.find('p', {'price'}).text
            cena = cena.replace(" ", "")
            cena = cena.replace("zł", "")
            cena = cena.replace("\t", "").replace("\r", "").replace("\n", "")

            tytul = ogloszenie.find('a', {'data-cy': 'listing-ad-title'}).text
            tytul = str(tytul.replace("\t", "").replace("\r", "").replace("\n", ""))

            link = ogloszenie.find('a', {'marginright5'})['href']
            link = link.replace("\t", "").replace("\r", "").replace("\n", "")

            file.write(tytul+'%'+cena+'%'+link+'\n')


scrapeAll()
