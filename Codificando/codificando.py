codificando = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",",","\n"]
frase = []
monte_frase = 0
while monte_frase != 28:
    monte_frase = int(input("Monte a sua frase(insira um valor inteiro): "))
    frase.append(monte_frase)
    if monte_frase > 30:
        print("Valor inválido, insira outro valor")
        frase.remove(monte_frase)
        continue
    else:
    #Bloco de código pego com IA, basicamente pega cada indice da lista de frase - que recebe apenas ints - e verifica a posição igual ao da lista codificando, que recebe as letras correspondentes.
        resultado = [codificando[num] for num in frase]
        frase_final = "".join(resultado)
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------


print(frase_final)
