#OPERACION DE FORMATO

#manipulador de texto nro 16
cad="TE EXTRAÑADO MUCHO"
print(cad.rjust(20))   #va correr 20 espacios a la derecha

#manipulador de texto nro 17
cad="TE EXTRAÑADO MUCHO"
print(cad.center(30))   #me a centrar la cadena

#manipulador de texto nro 18
numero="8"
print(numero.zfill(4)) #me imprimira ceros a la isquierda de 8

#manipulador de texto nro 19
msg="precio del {celular}"
print(msg.format(celular="samsung"))

#manipulador de texto nro 20
msg="precio del {celular}"
marca="samsung"
print(msg.format(celular=marca))

#manipulador de texto nro 21
msg="hola {} tu nota es {}"
print(msg.format("julian","16"))

#manipulador de texto nro 22
msg="el cumpleaños de {1} es el dia {0}" #-> los valores de la cadena
print(msg.format("carlos","25"))  #toma los valores ordenados

#manipulador de texto nro 23
marca="adidas"
msg="la marca de tus zapatillas es {}"
print(msg.format(marca))

#manipulador de texto nro 24
msg="hola {} tu nota es {}"
nombre="elmer"
nota="20"
print(msg.format(nombre,nota))

#manipulador de texto nro 25
msg="como estas {0:20}"
print(msg.format("hermosa"))

#manipulador de texto nro 26
msg="como estas {0:>20}"
print(msg.format("hermosa"))

#manipulador de texto nro 27
msg="hay {:d} ingresantes a la escuela de ingenieria electronica"
print(msg.format(40))

#manipulador de texto nro 28
cad1="BOLETA DE VENTAS "
print("#"*30)
print(cad1.center(30))
informacion="el producto {} tien el precio de {}"
producto="huevos"
precio=5
print(informacion.format(producto,precio))

#manipulador de texto nro 29
ingrediente_1="cebolla"
ingrediente_2="pollo"
ingrediente_3="arroz"

ingredientes="el {} es utilizado con la {} y con el {}"
print(ingredientes.format(ingrediente_2,ingrediente_1,ingrediente_3))

#manipulador de texto nro 30
marcas="la marcas de ropa son {0} , {1} ,{2}."
print(marcas.format("nike","puma","adidas"))
