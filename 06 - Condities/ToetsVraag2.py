lengte = float(input('de gelijke lengte van beide personen: '))
naam1 = input('de naam van de eerste persoon: ')
gewicht1 = float(input('het gewicht van de eerste persoon:'))
naam2 = input('de naam van de tweede persoon: ')
gewicht2 = float(input('het gewicht van de tweede persoon: '))

bmi1 = int(gewicht1) / (int(lengte) * int(lengte))
bmi2 = int(gewicht2) / (int(lengte) * int(lengte))

hoogste_bmi = max(str(bmi1, str(bmi2)))

if bmi1 > bmi2:
    conclusie = naam1 + 'heeft het hoogste BMI' + str(bmi1) + 'en'

else:
    conclusie = naam1 + 'heeft het hoogste BMI' + str(bmi1) + 'en'

if hoogste_bmi < 18.5:
indicatie = 'heeft ondergewicht'

    elif hoogste_bmi < 25:
    indicatie = 'heeft een gezond gewicht'

    elif hoogste_bmi < 30:
    indicatie = 'heeft overgewicht'

    elif hoogste_bmi >= 30:
    indicatie = 'is obees'

print (conclusie + indicatie)










