def adicionar_notas(listaNotas):
        numLista = int(input("Insira um valor: "))
        if numLista > 10:
                print("Insira um valor válido: ")
                numLista = int(input("Insira outro valor: "))
                while numLista > 10:
                    print("Insira um valor válido: ")
                    numLista = int(input("Insira outro valor: "))
                    if numLista <= 10:
                        listaNotas.append(numLista)
        else:
            listaNotas.append(numLista)
            print("Valor válido!")  

def calcular_media(listaNotas):
        somaNotas = sum(listaNotas) / len(listaNotas)
        print("A média desses números é {:.2f}".format(somaNotas))

def main():
     listaNotas = []
     while True:
        print("""
        1 - Adicionar notas;
        2 - Liste essas notas;
        3 - Calcular Média;
        4 - Maior e Menor nota;
        5 - Fim;
        """)
        opcao = int(input("Insira um valor para iniciar o programa: "))
        if opcao == 1:
            adicionar_notas(listaNotas)
        elif opcao == 2:
            print(f"A ordem crescente das notas é essa aqui: {sorted(listaNotas)}")
        elif opcao == 3:
            calcular_media(listaNotas)
        elif opcao == 4:
            print(f"O maior número da lista é: {max(listaNotas)}")
            print(f"O menor número da lista é: {min(listaNotas)}")
        elif opcao == 5:
            print("Fim do programa...")
            print(listaNotas)
            break
        else:
            print("Opção inválida, tente de novo.")
if __name__ == '__main__':
    main()