import bs4, requests, smtplib, time

pageNum = 100
baseURL = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/?page='

def scrapeAll():
    totalOgloszenia = 0
    for x in range (1, pageNum):
        requestURL = requests.get(baseURL + str(x))
        print(f"{baseURL + str(x)} status: {requestURL.status_code}")
        requestURL.encoding = 'utf-8'
        soupParser = bs4.BeautifulSoup(requestURL.text, 'html.parser')
        ogloszenia = soupParser.find_all('table', {'summary': 'Ogłoszenie'})

        with open('data.txt', 'a', encoding="UTF-8") as file:
            for ogloszenie in ogloszenia:
                totalOgloszenia += 1
                cena = ogloszenie.find('p', {'price'}).text
                cena = cena.replace(" ", "")
                cena = cena.replace("zł", "")
                cena = cena.replace("\t", "").replace("\r", "").replace("\n", "")

                tytul = ogloszenie.find('a', {'data-cy': 'listing-ad-title'}).text
                tytul = str(tytul.replace("\t", "").replace("\r", "").replace("\n", ""))

                link = ogloszenie.find('a', {'marginright5'})['href']
                link = link.replace("\t", "").replace("\r", "").replace("\n", "")

                file.write(tytul+'%'+cena+'%'+link+'\n')

    print(totalOgloszenia)

scrapeAll()
