def BinarioAcomplementoMagnitudSigno(binario):
    if binario[0] == '0':
        return 'Complemento a magnitud y signo: ' + binario
    else:
        magnitud = binario[1:]
        signo = '-' + binario[1:]
        return 'Complemento a magnitud y signo: ' + signo

def binarioAcomplementoDos(binario):
    if binario[0] == '0':
        return 'Complemento a dos: ' + binario
    else:
        complementoUno = ''.join(['1' if i == '0' else '0' for i in binario])
        complementoDos = binarioAdecimal(complementoUno) + 1
        return 'Complemento a dos: ' + decimalAbinario(complementoDos)

def binarioAdecimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[-(i+1)]) * 2**i
    return decimal

def decimalAbinario(decimal):
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    binario = '0' * (8 - len(binario)) + binario
    return binario

# Ejemplo de uso
binario = input('Ingrese un número binario de 8 bits: ')
print(BinarioAcomplementoMagnitudSigno(binario))
print(binarioAcomplementoDos(binario))


BinarioAcomplementoMagnitudSigno(binario)