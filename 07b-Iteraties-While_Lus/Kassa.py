eindbedrag = 0

prijs = int(input('Wat is de prijs van het product? '))

while prijs > 0:
    eindbedrag += prijs
    prijs = int(input('Wat is de prijs van het product? '))

if prijs <= 0:
    print('De totale prijs is € ' + (str(float(eindbedrag)))

