import operacoes

t = operacoes.titulo("Calculadora Simples em Python")
c = int(input('''Digite o código para sabermos qual operação você está querendo efetuar:
[1] - Soma             [5] - Raiz Quadrada
[2] - Subtração        [6] - Seno
[3] - Divisão          [7] - Cosseno
[4] - Multiplicação    [8] - Tangente

Digite aqui para sabermos: '''))
if c == 1:
    a, b = map(int, input(f"Insira aqui os valores de A e B: ").split())
    resul = operacoes.soma(a,b)
    print(f"{a} + {b} = " ,resul)
if c == 2:
    a, b = map(int, input(f"Insira aqui os valores de A e B: ").split())
    resul = operacoes.sub(a,b)
    print(f"{a} - {b} = " ,resul)
if c == 3:
    a, b = map(int, input(f"Insira aqui os valores de A e B: ").split())
    resul = operacoes.divisao(a,b)
    print(f"{a} : {b} = " ,resul)
if c == 4:
    a, b = map(int, input(f"Insira aqui os valores de A e B: ").split())
    resul = operacoes.mult(a,b)
    print(f"{a} X {b} = " ,resul)
if c == 5:
    a = float(input(f"Insira aqui o valor de A: "))
    resul = operacoes.raizquadrada(a)
    print("A Raiz Quadrada de {:.0f} é {:.4f}".format(a,resul))
if c == 6:
    a =  float(input(f"Insira aqui o valor de A: "))
    resul = operacoes.sin(a)
    print("O Seno de {:.0f} é {:4f}".format(a ,resul))
if c == 7:
    a = float(input(f"Insira aqui o valor de A: "))
    resul = operacoes.cos(a)
    print("O Cosseno de {:.0f} é {:.4f}".format(a,resul))
if c == 8:
    a =  float(input(f"Insira aqui o valor de A: "))
    resul = operacoes.tg(a)
    print("A Tangente de {:.0f} é {:.4f}".format(a,resul))
