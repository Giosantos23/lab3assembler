def menu():
    print("Bienvenido al sistema de conversión")
    print('\t1 - hola, bienvenido a la conversión de decimal a hexadecimal')
    print('\t2 - hola, bienvenido a la conversión de hexadecimal a decimal')
    seleccion = input('Ingrese opcion 1 si desea convertir de decimal a hexadecimal o la opcion 2 si es viceversa')
    if seleccion == '1':
        decia_exa()
    elif seleccion == '2':
        exaa_deci()
    else:
        print('Seleccione 1 o 2')
    menu()
def decia_exa():
    deci=int(input('Ingrese el numero decimal (sin espacios) que desea convertir: '))
    hexi=hex(deci)
    print('El decimal convertido es: ',hexi)

def exaa_deci():
    hexa = input('Ingrese el hexadecimal (en mayusculas) que desea convertir: ').strip().upper()
    decimal = int(hexa, base=16)
    #Se utiliza funcion de base 16, la que los hexadecimales tienen
    print('El hexadecimal convertido es:', decimal)
menu()