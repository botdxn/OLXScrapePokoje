import bs4, requests, time, threading, concurrent.futures, re, os
from datetime import datetime

pageNum = 5
baseURL = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/?page='
URLList = []

def scrapeAll():
    for x in range (1, pageNum):
        print(f"Tworzenie cache linków ogłoszeń...{x}")
        os.system('cls')
        requestURL = requests.get(baseURL + str(x))
        print(f"{baseURL + str(x)} status: {requestURL.status_code}")
        requestURL.encoding = 'utf-8'
        soupParser = bs4.BeautifulSoup(requestURL.text, 'html.parser')
        ogloszenia = soupParser.find_all('table', {'summary': 'Ogłoszenie'})

        for ogloszenie in ogloszenia:
            link = ogloszenie.find('a', {'marginright5'})['href']

            if str(link) in URLList:
                pass
            else:
                URLList.append(link)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(requestSingle, URLList)

def requestSingle(link):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")
    filename = 'data_' + str(dt_string) + '_' + str(pageNum) + '.txt'
    with open(filename, 'a', encoding="UTF-8") as file:
        try:
            typPokoju = ''
            requestSingle = requests.get(link)
            print(f"{link} status: {requestSingle.status_code}")
            requestSingle.encoding = 'utf-8'

            soupParser = bs4.BeautifulSoup(requestSingle.text, 'html.parser')
            try:
                typPokoju = soupParser.find_all('table', {'class': 'item'})[2]
                typPokoju = typPokoju.find('a').text
                typPokoju = typPokoju.replace("\t", "").replace("\r", "").replace("\n", "")
            except:
                typPokoju = "Brak danych"

            cena = soupParser.find('div', {'class': 'price-label'}).text
            cena = cena.replace(" ", "")
            cena = cena.replace("zł", "")
            cena = cena.replace("\t", "").replace("\r", "").replace("\n", "")

            tytul = soupParser.find('div', {'class': 'offer-titlebox'})
            tytul = tytul.find('h1').text
            tytul = str(tytul.replace("\t", "").replace("\r", "").replace("\n", ""))
            tytul = tytul.strip()


            file.write(tytul+'%'+cena+'%'+link+'%'+str(typPokoju)+'\n')
            file.close()
            os.system('cls')
        except:
            pass

scrapeAll()
