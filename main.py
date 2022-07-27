print("Hola Mundo con Python")

miVariable = "Hola Mundo desde una variable"
print(miVariable)
print(miVariable)
print(miVariable)

miVariable = 3005
print(miVariable)
print(miVariable)
print(miVariable)

x = 10
y = 2
z = x + y
print(z)
print(id(z)) #la funcion id nos regresa la direccion de memoria donde se encuentra guardada el valor de z

nombre = "Juan Lara"
telefono = 8136956121
email = "max_lara3005@hotmail.com"
print(nombre)
print(telefono)
print(email)

print(type(nombre))

x = True
print(type(x)) #Las literales true y false deben llevar la primera letra mayuscula

numero1 = "1"
numero2 = "2"
print(numero1 + numero2)
print(int(numero1) + int(numero2))

numero1 = 1
numero2 = 2
print(numero1 + numero2)

#Tipo bool
miVariable = True
print(miVariable)
miVariable = 3 > 2
print(miVariable)

if miVariable:
    print("El resultado es Verdadero")
else:
    print("El resultado es Falso")

#Funcion input para procesar entrhoada de usuario
resultado = input("Escribe un mensaje: ")
print(resultado)
print("Fin del programa")

primerNumero = int(input("Escribe primer numero:"))
segundoNumero = int(input("Escribe segundo numero:"))
resultado = primerNumero + segundoNumero
print("El Resultado de la suma es: ", resultado)