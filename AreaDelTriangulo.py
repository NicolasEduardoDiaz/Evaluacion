# Allar el area de un triangulo
# El area de un triangulo es (base*altura)/2

print("Hola usuario, este programa es para allar el area de un triangulo")
print("Dame la base y la altura y te dire su area")

base = int(input())
altura = int(input())

area = (base*altura)/2

if area > 1000:
     print("Datos no validos ")
    
else:
    print("el area es ", area, " metros cuadrados")