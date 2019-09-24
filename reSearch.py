import re

metraz = '''Wynajmę pokój 1 osobowy 12m2 internet + TV w 3 pokojowym mieszkaniu 65m2 na ul. Orzechowej

Sklepy: ferio gaj, hala gaj, biedronka, kaufland, lidl, żabka, hala kupców, sklep osiedlowy.

Komunikacja: autobusy K, 136, 145, 146, tramwaje 31,32
ul. Orzechowa, Świeradowska

Opieka zdrowotna: ul. Krynicka, Borowska.

Cena bez żadnych dodatkowych opłat wynosi 900 zł + kaucja

Dla osób które cenią sobie ciszę, nie palących, dbających o czystość.

Więcej informacji tel.12 m^2'''

s2 = ['']

r1 = re.findall(r"\d{1,2}m2|\d{1,2}m\s2|\d{1,2}m\^2|\d{1,2}\sm\^2|\d{1,2}mkw|\d{1,2}dm\skw|\d{1,2}m|\d{1,2}\sm", metraz)
print(f'\n==={r1}===\n')
for element in r1:
    try:
        element = element.replace("m2", "")
        element = element.replace("m 2", "")
        element = element.replace("m^2", "")
        element = element.replace("m ^2", "")
        element = element.replace("mkw", "")
        element = element.replace("m kw", "")
        element = element.replace("m", "")

        if int(element) < 20:
            #print(element[0])
            metraz = element
        else:
            metraz = 'Brak danych'
    except ValueError:
        pass

print(metraz)
