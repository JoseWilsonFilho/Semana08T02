def numero_inteiro(numero):
    if numero % 3 == 0 and not numero % 5 == 0:
        return 'FIZZ'
    elif numero % 5 == 0 and not numero % 3 == 0:
        return 'BUZZ'
    elif numero % 3 == 0 and numero % 5 == 0:
        return 'FIZZBUZZ'
    else:
     return numero
       
numero = int(input())
numero = numero_inteiro(numero)
print(numero)


