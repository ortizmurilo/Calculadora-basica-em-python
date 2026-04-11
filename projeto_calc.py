def somar(a,b):
    return a+b
def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if a == 0:
        return 'Erro, dividendo é igual a 0, tente novamente'
    elif b == 0:
        return 'Erro, divisor é igual a 0, tente novamente'
    else:
        return a/b

def menu():
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
while True:
    menu()
    try:
        operacao = int(input("Escolha a operação: "))
    except ValueError:
        print('Tente digitar apenas numeros.')
        continue
    try:
        a = int(input('Digite um numero inteiro para o primeiro elemento:'))
        b = int(input('Digite um numero inteiro para o segundo elemento:'))
    except ValueError:
        print("Digite apenas números!")
        continue

    if operacao == 1:
        resultado = (somar(a,b))
    elif operacao == 2:
        resultado = (subtrair(a,b))
    elif operacao == 3:
        resultado = (multiplicar(a,b))
    elif operacao == 4:
        resultado = (dividir(a,b))
    else:
        print('Não há operação para realizar com o número digitado')
    print(f'O resultado da operação é {resultado}')
    if input('Deseja realizar outra operação?[s/n]') == 'n':
        break

