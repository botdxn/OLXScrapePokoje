# OLXScrapePokoje
Scraping OLX when searching for rooms to lease.

# Opis skryptu
Crawler umożliwia ściągnięcie ogłoszeń zamieszczanych w serwisie OLX poprzez podanie adresu bazowego np. 'https://www.olx.pl/nieruchomosci/stancje-pokoje/wroclaw/?page=' bez końcówki identyfikującej numer obecnej strony. Następnie w skrypcie podajemy ilość stron, które chcemy ściągnąć a skrypt samemu ściągnie tytuły, ceny i linki ogłoszeń i zapisze je w pliku .txt gotowym do obróbki w np. Excelu.

# Wydajność
Dla komputera z procesorem Ryzen 5 1600 prędkość wykonania skryptu dla pageNum = 100 wyniosła ok. 313 sekund.

# Wykorzystane moduły
Z modułów, które nie są automatycznie dołączane do instalacji Pythona to jedynie BeautifulSoup i concurrent.futures

# To do
- Zaimplementować wielowątkowość podczas wstępnego cache'owania linków
- Analiza poprzez pandas (zamiast używania Excela)
- Stworzyć frontend (np. Flask lub Django) do scrape'owania i wyświetlania wykresów dla podanej lokalizacji (np. Legnica, Wrocław, Poznań itd)
