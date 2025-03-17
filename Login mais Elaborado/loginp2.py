''

def nome(person):
    name = str(input("Insira seu nome: "))
    person.append(name)

def gmail(person):
    prefixo = '@gmail.com'
    validador = len(prefixo) 
    ultimos_caracteres = prefixo[-validador:]
    gmailValidador = str(input('Insira seu Gmail para Login: '))
    if gmailValidador.endswith(ultimos_caracteres) == True:
        person.append(gmailValidador)
        print("Gmail validado...")
    else: 
        print("Gmail inválido...")
        gmailValidador = str(input("Insira seu Gmail novamente: "))
        while gmailValidador.endswith(ultimos_caracteres) == False:
            gmailValidador = str(input("Insira outro Gmail: "))
            if gmailValidador.endswith(ultimos_caracteres):
                person.append(gmailValidador)
                print("Gmail válido!")
                break

def CPF(person):
    while True:
        cpf = input("Insira seu CPF: ")
        
        if len(cpf) == 11 and cpf.isdigit():
            print("CPF validado...")
            person.append(cpf)
            break
        else:
            print("CPF inválido! Tente novamente.")
#Precisei de ajuda de IA para fazer. Basicamente, no print final da lista, separa ela de 3 em 3 dados pedidos
def dividir_lista(person):
     for i in range(0, len(person), 3):
        print(' - '.join(map(str, person[i:i+3])))

def main():
    print("=+="*20)
    print("TELA DE LOGIN")
    print("=+="*20)
    person = []
    registros = 0
    insercaoRegistro = 'S'
    while insercaoRegistro == 'S':
        insercaoRegistro = str(input("Você deseja inserir um novo login > S - [Sim] | N - [Não]: "))
        if insercaoRegistro == 'N' or insercaoRegistro == 'n':
            print("Código Finalizado...")
            break
        else:
            nome(person)
            print("=+="*20)
            gmail(person)
            print("=+="*20)
            CPF(person)
            registros += 1
        print('====TELA DE REGISTRO====')
        print(('\n----------------------|\n'.join(person)))    
        print('-----------------------------')    
        print(f"Foram registrados um número total de {registros} registro(s).")
        print('========================')
    print("===Tela de Registros. FINAL===")
    # Printa o registro final em 3 em 3
    dividir_lista(person)
    print('===============================')

    
if __name__ == '__main__':
    main()

