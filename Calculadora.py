import math as mt
print("Calculadora")
a = int(input("Primer valor: "))
b = float (input("Segundo valor : "))
operacion = input ("Operacion (+,-,*,/,^,F) : ")
if operacion == "+" :
    print("El resultado es : " , a + b)
if operacion == "-" : 
    print("El resultado es :", a - b )
if operacion == "*" :
    print("EL resultado es :" , a * b )
if operacion == "/" : 
    if b != 0: 
        print("El resultado es :" , a / b )
    else:
        print("Error, no se puede dividir entre cero")
if operacion == "^" :
     print("El resultado es : " , a ** b )
if operacion == "F" :
    print("Para factorial el segundo valor no sera utiliado")
    print("El resultado es : " , mt.factorial(a) )
    