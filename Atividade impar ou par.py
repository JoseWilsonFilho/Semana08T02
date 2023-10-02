# Definição da varável para a importação dos dados do usuário
numero_inteiro = int(input())

# Definição da condição caso o numero colocado seja impar ou par
if numero_inteiro %2 != 0:
    impar = numero_inteiro + 8
    print(impar)
elif numero_inteiro %2 == 0:
    par = numero_inteiro + 5
    print(par)
    

