# Como crear un diccionario

Marca_Carro={1:"Honda",2:"Toyota",'codi1':"MERCEDES",'Codi2':"Macerati"}
print(Marca_Carro)

#Modificar elementos de un diccionario
print("")
print("")
print("")
Marca_Carro[2]="Subaru"
print("Este es el diccionario modificado: ",Marca_Carro)
# Agregar elementos
print("")
print("")
print("")
Marca_Carro['Codig3']=("Kia")
print(Marca_Carro)

# Copiar tabla o diccionario

DICCIONARIO1=Marca_Carro.copy()
print("Diccionario copiado",DICCIONARIO1)

#Oteniendo el valor diccionario por su clave
print("Esta clave le corresponde el dato: ",Marca_Carro['Codig3'])

#Optener valor con get

print("El valor a buscar es: ",DICCIONARIO1.get('Codi2'))























