speler1 = input('blad, steen of schaar? ')
speler2 = input('blad, steen of schaar? ')

if speler1 == speler2:
    print('onbeslist')

else:
    if (speler1 == 'blad' and speler2 == 'steen') or (speler1 == 'steen' and speler2 == 'schaar') or (speler1 == 'schaar' and speler2 == 'blad'):
        print('speler 1 wint')

    elif (speler2 == 'blad' and speler1 == 'steen') or (speler2 == 'steen' and speler1 == 'schaar') or (speler2 == 'schaar' and speler1 == 'blad'):
        print('speler 2 wint')
    else:
        print('leer typen')

