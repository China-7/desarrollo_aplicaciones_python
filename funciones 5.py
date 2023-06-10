def contar():
      a=int(input("Introduce un numero par"))
      print("")
      if a%2==0:
            print("Muy bien",a, "es  un numero par")
      else:
            print("lo siento ",a,"no es un numero par")
            print("Vuelve a intentarlo")
            a=int(input("Introduce un numero par"))
            print("")
            if a%2==0:
                  print("Muy bien",a, "es  un numero par")
contar()
