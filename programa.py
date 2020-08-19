
"""
    Algoritimo
"""

# Variavel que armaze a lista de numeros
valoresArmazenadosK = []
def main():
    condicaoLoop: int = 1

    while condicaoLoop != 0:
        print("\n\tProblema do conjunto e seus elementos únicos")
        print("\n\tPor definição, um conjunto não pode ")
        execucaoCodigo()

        condicaoLoop = int(input("\tDigite qualquer numero diferente de '0' para executar novamente!"))
        pass

    print("\tO programa foi finalizado com sucesso!")
    pass

def execucaoCodigo():
    quantidadeDeLeituraEmK: int = 0
    while quantidadeDeLeituraEmK == 0 or quantidadeDeLeituraEmK < 1 or quantidadeDeLeituraEmK > 1000:
        quantidadeDeLeituraEmK = int(input("\n\tDigite um numero no intervalo de 1 a 1000: "))
    for index in range(1, quantidadeDeLeituraEmK+1):
        leitura = int(input(f"\n\t({(index)}) Digite um numero no intervalo de -1000 a 1000: "))
        verificao(leitura)
        pass
    imprimirNumeros()

def verificao(num:int):
    status = False
    for n in valoresArmazenadosK:
        if num == n or num < -1000 or num > 1000:
            status = True
    if status == False:
        valoresArmazenadosK.append(num)
    pass


def imprimirNumeros():
    valoresArmazenadosK.sort()
    for numero in valoresArmazenadosK:
        print(f"\n\t\t -- {numero} -- ")
    pass


main()