# Vraagt de coëfficiënten bij x^2, x^1 en x^0 van tweedegraadsfunctie f(x) = ax^2 + bx^1 + cx^0
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

# bereken de discriminant
discriminant = b ** 2 - (4 * a * c)

#uitvoer
print('discriminant = ', discriminant)

#-------------------------------------

print('discriminant= ', float(input('b: ')) ** 2 - 4 * float(input('a: ')) * float(input('c: ')))