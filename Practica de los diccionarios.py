print("DICCIONARIO, LISTAS Y TUPLAS")

print("TABLAS")


print("Diccionario")

Profesores={ 1:"Cela" , 2:"Martin" , 3:"Victor", 4:"Andrea" , 5:"Mariluz" , 6:"Juana" , 7:"Miguelina" }

"""
Buscar el elemento Mariluz
"""

print("Estoy buscando el elemento: ", Profesores[5] )


"""
Agregar el elemento Veras
"""

Profesores[8]='Veras'
print(Profesores)


print("Lista")

Profesores1=["Cela", "Martin","Victor","Andrea", "Mariluz","Juana","Miguelina" ]
print(Profesores1)

#Remplazando el elemento Miguelina

Profesores1[6]='Josefina'
print(Profesores1)

#Cuantos elementos tiene la lista

print(len(Profesores1))

#Eliminar  el elemento Victor

Profesores1.remove('Victor')
print(Profesores1)


print("Tupla")

Profesores3=("Cela", "Martin","Victor","Andrea", "Mariluz","Juana","Miguelina" )

print(Profesores3)

#Cuantos elementos tiene la tupla

print(len(Profesores3))

print("El elemento que esta en la posicion 4 es: ",Profesores3[4])


print("El elemento que esta en la posicion 2 es: ",Profesores3[2])







































