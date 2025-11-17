import random
print("Generador de números aleatorios")
limiteBajo = int(input("¿Cuál quieres que sea el número más bajo posible? "))
limiteAlto = int(input("¿Cuál quieres que sea el número más alto posible? "))
numero = random.randint(limiteBajo, limiteAlto)
print("Tu número es", numero)
