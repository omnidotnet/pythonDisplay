a = int(input('a = '))
b = int(input('b = '))
op = input('suma/resta/multiplicación/división: ')
if op == 'suma':
    c = a + b
elif op == 'resta':
    c = a - b
elif op == 'multiplicación':
    c = a * b
elif op == 'división':
    c = a / b
else:
    c = 'Error'
print('Respuesta = ',c)
