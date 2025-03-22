"""EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia,
    bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...

- Debes hacer print por consola del resultado de todos los ejemplos.
 
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
Seguro que al revisar detenidamente las posibilidades has descubierto algo 
nuevo.
"""

# asignacion

a = 23
b = 25
c = [1,2,3,4,5]

#Aritmeticos

resultado1= a + b
resultado2 = a * b 
resultado3 = a//b 
resultado4 = a**b 

print(f'\nLa suma es: {resultado1}, la multiplicacion es: {resultado2}, la division enteera es: {resultado3}, el exponente es. {resultado4}')
print('\n-----------------------\n')

# condicionales
if b < a:
    print(True)
else:
    print(False)

if a < b:
    print(True)
else:
    print(False)

if a == b:
    print(True)
else:
    print(False)
print('\n-----------------------\n')

for i in c: #imprime la multiplicacion de cada  elemento de la lista por la longitud de la lista
    print(i*len(c))
print('\n-----------------------\n')
    

for o in range(10,56):
    if o % 2 == 0 and o  != 16 and o %3 == 0:
        print (o)
