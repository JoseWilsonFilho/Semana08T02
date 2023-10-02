# Definição da função para relacionar homems e mulheres com o peso ideal dado na questão
def peso(sexo, altura):
    if sexo== 1:
        return (72.7 * altura ) - 58
    elif sexo == 2:
        return (62.1 * altura ) - 44.7
    else:
        return 0

# Definição das variáveis para a importação dos dados do usuário    
altura = float(input())
sexo = int(input())
peso_ideal = peso(sexo, altura)
print(f'{peso_ideal:.2f}')