#Elaborar un programa en py que permita gestinar una tienda d videojuegos donde se presetan y devuelven los mismos

cons_existenciasInt = 5
var_cantidadInt = int(input('Ingrese la cantida de videojuegos a prestar -> '))
if var_cantidadInt <=0:
    print ('La cantidad de videojuegos debe ser mayor que 0')
else:
    if var_cantidadInt <= cons_existenciasInt:
        print ('Tu prestamo ha sido aprobado')
        print ('Existencias actuales: ',(cons_existenciasInt - var_cantidadInt))
        enter = input('Presione <ENTER> para continuar')       
    else:
        print ('No podemos prestarte esa cantidad de videojuegos')
    
    