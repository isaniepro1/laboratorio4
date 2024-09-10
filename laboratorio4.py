#1
#fibonacci

#recursion con memoizacion

def fibonacci(n,memo={}):
    if n in memo:
        return memo [n]
    if n <=1:
        return n
    memo[n]= fibonacci(n-1,memo) + fibonacci(n-2,memo)
    return memo[n]
resultado= fibonacci(50)
print("Fibonacci e 50 es:",resultado)

#2
#Uso avanzado de float con manejo de precision decimal
from decimal import Decimal, getcontext

getcontext().prec=50
numero1=Decimal('1.123456789123456789')
numero2=Decimal('2.987654321987654321')

resultado =numero1 * numero2

print(f"Resultado preciso:{resultado}")

#3
import re
# Usamos una expresión regular avanzada para extraer palabras en mayúsculas de una cadena
cadena = "ESTO es un EJEMPLO de uso AVANZADO de CADENAS y Expresiones REGULARES."
# Expresión regular que busca palabras completamente en mayúsculas
patron = r'\b[A-Z]{2,}\b'
# Encontramos todas las coincidencias
palabras_mayusculas = re.findall(patron, cadena)
print("Palabras en mayúsculas:", palabras_mayusculas)

#4
def sumar_o_default(a,b):
    return (a or 0) + (b or 0)

print(sumar_o_default(5, None))
print(sumar_o_default(None,None))
print(sumar_o_default(10,20))