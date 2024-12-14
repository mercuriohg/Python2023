import moeda

t = moeda.titulo("Conversor de Moedas")
escolha = int(input('''Deseja converter o BRL para qual moeda: 
[1] - Dólar
[2] - Euro
[3] - Libra
[4] - Iene
Insira a conversão que queira: '''))
if (escolha == 1):
    valor = float(input('Insira o valor em BRL: '))
    dolar = moeda.dolar(valor)
    print(f'O valor em Dólar é US$ {dolar:.2f}')
elif (escolha == 2):
    valor = float(input('Digite o valor em BRL: '))
    euro = moeda.euro(valor)
    print(f'O valor em Euro é € {euro:.2f}')
elif (escolha == 3):
    valor = float(input('Digite o valor em BRL: '))
    libra = moeda.libra(valor)
    print(f'O valor em Libra é £ {libra:.2f}')
elif (escolha == 4):
    valor = float(input('Digite o valor em BRL: '))
    iene = moeda.iene(valor)
    print(f'O valor em Iene é ¥ {iene:.2f}')
