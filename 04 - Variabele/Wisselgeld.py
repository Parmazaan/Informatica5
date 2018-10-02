bedrag = (int(input('bedrag = ')))

uitkomst = (str(bedrag) + ' cent kan je omwisselen in ')
uitkomst += (str(bedrag // 100 + (bedrag % 100) // 50 + (bedrag % 50) // 20 + (bedrag % 50 % 20) // 10 + (bedrag % 50 % 20 % 10) // 5 + (bedrag % 50 % 20 % 10 % 5) // 2 + (bedrag % 50 % 20 % 10 % 5 % 2) // 1))
uitkomst += (' muntstukken ')

print(uitkomst)


