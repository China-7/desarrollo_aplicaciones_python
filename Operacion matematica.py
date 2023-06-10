#Mandato del programa
"""
print("")
print("")
print("Crear un programa y usar los operadores ya vistos en clases que liste")
print("  un menu de opciones donde permite elegir que operacion matematica  ")
print("   realizar como son sumar , restar multiplicar y dividir ")
"""
print("---------------------------------------------------------------------------")
print("")
print("                     Bienvenid@ a su sistema sig                           ")
print("")
print("---------------------------------------------------------------------------")
print("")
print("1.Realizar una suma")
print("2.Realizar una resta")
print("3.Realizar una Multiplicacion")
print("4.Realizar una Division")
print("4.Cerrar el programa")
print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")
print
nn=int(input("Seleciona la operacion a realizar:  "))
print("------------------------------------------------------------------------------")
print("")
("")
    
if nn==0:
         print("Esta opcion no es valida elija una del 1 al 5")
         nn=int(input("Seleciona la operacion a realizar:  "))


elif nn<=4:   
        n1=int(input("Introduzca el primer numero:  "))
        n2=int(input("introduzca el segundo numero:  "))
op=0
while op<=0:
    

    if nn==1:
        SUMAR=n1+n2
        print("La respuesta es: ",SUMAR)
        break
    #Resta

    if nn==2:
        Resta=n1-n2
        print("La repuesta es: ",Resta)
        break

#multiplicacion

    if nn==3:
        Multiplicacion=n1*n2
        print("La respuesta es: ",Multiplicacion)
        break

#Aqui empieza la toma de decision si elige dividir

    if nn==4:

#AQUI SE  VERIFICA SI EL DENOMINADOR ES 0 PARA PREVENIR ERROR
     if n2==0:
            print("-----------------------------------------------------------------------------")
            print("")
            print("ERROR ERROR, NO SE PUEDE DIVIDIR ENTRE CERO.")
            print("")
           
         
        
#Aqui se verifica si el denominador es diferente de cero     

    if n2!=0:
       Divide=n1/n2
       print("El resultado es: ",Divide)
       print("")
       print("Cerrando el programa")
       break

       

    if nn==5:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("")
        print("finalizando el programa")
        print("")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        break





















    



















