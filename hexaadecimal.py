def menu():
    print("Bienvenido al sistema de conversión")
    print('\t1 - hola, bienvenido a la conversión de decimal a hexadecimal')
    print('\t2 - hola, bienvenido a la conversión de hexadecimal a decimal')
    seleccion = input('Ingrese opcion 1 si desea convertir de decimal a hexadecimal o la opcion 2 si es viceversa')
    if seleccion == '1':
        print('o')
        decia_exa()
    elif seleccion == '2':
        exaa_deci()
    else:
        print('Seleccione 1 o 2')
    menu()
def decia_exa():
    print('hey')
def exaa_deci():
    hexa = input('Ingrese el numero hexadecimal (en mayusculas) que desea convertir: ').strip().upper()
    decimal = int(hexa, base=16)
    #Se utiliza funcion de base 16, la que los hexadecimales tienen
    print('El decimal convertido es:', decimal)
menu()