#Definir un diccionario
lista={"Clave1":"Alex","Clave2":24,"Clave3":1.67,"Clave4":True}
print(lista)
lista["Clave4"]=False
lista["Clave5"]=True
#Optener un valor de acuerdo a su clave
print("El valor es: ",lista["Clave1"])
print("Lista Actualizada",lista)

#Copiar tabla
otra_lista=lista.copy()