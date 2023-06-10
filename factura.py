nom_cli=input("Cual es el nombre: ")
num_fac=input("Numero factura: ")
precio_art=int(input("precio: "))
cant_art=int(input("Cantidad de articulos: "))

total_neto=precio_art*cant_art

if total_neto >= 5000:
    des1=total_neto * 10/100
    total_pagar=total_neto-des1
    print("nombre: ",nom_cli)
    print("Numero factura: ",num_fac)
    print("Cantidad de articulos: ",cant_art)
    print("Precio: ",precio_art)
    print("Total neto: ", total_neto)
    print("total a pagar: ",total_pagar)

else:
    des2=total_neto*5/100
    total_pagar=total_neto-des2
    print("nombre: ",nom_cli)
    print("Numero factura: ",num_fac)
    print("Cantidad de articulos: ",cant_art)
    print("Precio: ",precio_art)
    print("Total neto: ", total_neto)
    print("total a pagar: ",total_pagar)
