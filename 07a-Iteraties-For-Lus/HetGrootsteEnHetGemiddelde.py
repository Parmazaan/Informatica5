aantal_getallen = int(input('aantal getallen: '))
som = 0
maximum = 0

for i in range(aantal_getallen):
    random_getal = int(input('getal: '))
    if i == 0:
        maximum = random_getal
    elif random_getal > maximum:
        maximum = random_getal
    som += random_getal

gemiddelde = (som/aantal_getallen)
print('Het grootste getal is {:d} en het gemiddelde is {:.2f}'.format(maximum, gemiddelde))