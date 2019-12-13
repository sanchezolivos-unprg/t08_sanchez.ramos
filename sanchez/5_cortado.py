# CORTADO DE CADENAS 1:
#     0         1         2         3         4         5         6
#     0123456789012345678901234567890123456789012345678901234567890123456
msg1="LA UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO SE ENCUENTRA EN LAMBAYEQUE"

# mostrar UNIVERSIDAD
print(msg1[3:14])

# mostrar OLLA
print(msg1[39:35:-1])

# mostrar PEDRO
print(msg1[24:29])

# CORTADO DE CADENAS 2:
#     0         1         2         3         4
#     012345678901234567890123456789012345678901234567
msg2="SI NO QUIERES SER DERROTADO, SOLO SIGUE ADELANTE"

# Mostrar la cadena: DERROTADO No
subcadena=msg2[18:27] + " " + msg2[3:5]
print(subcadena)
