# ENTREVISTA

nombre = input("Hola mucho gusto, ¿cual es tu nombre?: ")

print("Un placer conocerte", nombre)

nombre = input("¿cuantos años tienes?: ")

print("okey entonces tienes",nombre,"años")

nombre = input("¿que es lo que te gusta hacer: ")

print("hooo genial, entonces te gusta",nombre)

nombre = input("¿cual es tu comida favorita?")

print("¡Genial!, que buenos gustos tienes,",nombre,"ami tambien me gusta")

################################################################################################################

# Multipicaciones

print("ingresa los numeros que deseas multiplicar")

a = float(input("a -> "))
b = float(input("b -> "))

resultado = a * b

print("el resultado es: ",resultado)

################################################################################################################

print("una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto"
      " devera pagar finalmente por su compra")

precio = float(input("Digite el precio: "))

descuento = precio * 0.15
precio_final = precio - descuento

print("el precio final a pagar es de $",precio_final)
