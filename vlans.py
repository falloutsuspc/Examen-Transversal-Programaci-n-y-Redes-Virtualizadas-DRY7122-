aclNum = int(input("Cual es el número de ID de la vlan? "))

if aclNum >= 1 and aclNum <= 1005:

  print("Es una Vlan de rango Normal .")

elif aclNum >=1006 and aclNum <= 4095:

  print("Es una Vlan de rango Extendida")

else:

  print("El número de Vlan ingresado es desconocida.")

