## 📖 Codificando mensagem.

Um código para testar minha lógica de programação - infelizmente não estou totalmente bom, pois peguei ref em um código de IA para facilitar, mas estou no caminho -. Basicamente o código contém uma lista com as letras e uma lista que serão adicionados valores inteiros, o código termina após ser posto o ponto final, <strong>código = 28</strong>. 

## 🗃️ Bloco que faz a verificação indice por indice.
```py
        resultado = [codificando[num] for num in frase]
        frase_final = "".join(resultado)
```
## ☑️ Código Final.

```py
codificando = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",","]
frase = []
monte_frase = 0
while monte_frase != 28:
    monte_frase = int(input("Monte a sua frase: "))
    frase.append(monte_frase)
    if monte_frase > 30:
        print("Valor inválido, insira outro valor")
        frase.remove(monte_frase)
        continue
    else:
        resultado = [codificando[num] for num in frase]
        frase_final = "".join(resultado)

print(frase_final)
```
>Cada dia estou em evolução constante.
