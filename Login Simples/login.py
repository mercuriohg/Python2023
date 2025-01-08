string = "@gmail.com"
n = len(string) 
ultimos_caracteres = string[-n:]
print("=+="*20)
print("TELA DE LOGIN")
print("=+="*20)
n =  input("Insira seu nome: ")
print("=+="*20)
cp = input("Insira seu CPF: ")
if len(cp) > 11 or len(cp) < 11:
    print("CPF invalidado!")
    cp = input("Insira novamente seu CPF: ")
    while len(cp) > 11 or len(cp)<11:
        print("CPF invalidado:")
        cp = input("Insira novamente seu CPF: ")
print("=+="*20)
gm = input("Insira seu email: ")
if gm.endswith(ultimos_caracteres):
    print("Gmail válido!")
else:
    print("Gmail inválido!")
    gm = input("Insira um Gmail válido: ")
    while gm.endswith(ultimos_caracteres) == False:
        if gm.endswith(ultimos_caracteres):
             print("Gmail válido!")
        else:
            print("Gmail inválido")
            gm = input("Insira outro Gmail: ")
cadastro = 1
n2 = "s"
print(f"{n}. {cp}. {gm}")
while n2 == "s":
    n2 = str(input("Gostaria de fazer mais um cadastro? s[sim] - n[não]: "))
    if n2== "n":
        break
    else:
        cadastro +=1 
        print("=+="*20)
        n = input("Insira seu nome: ")
        print("=+="*20)
        cp = input("Insira seu cpf: ")
        if len(cp) > 11 or len(cp) < 11:
            print("CPF invalidado!")
            cp = input("Insira novamente seu cpf: ")
            while len(cp) > 11 or len(cp)<11:
                print("CPF invalidado:")
                cp = input("Insira novamente seu cpf: ")
        print("=+="*20)
        gm = input("Insira seu gmail: ")
        if gm.endswith(ultimos_caracteres):
            print("Gmail válido!")
        else:
            print("Gmail inválido!")
            gm = input("Insira um Gmail válido: ")
            while gm.endswith(ultimos_caracteres) == False:
                if gm.endswith(ultimos_caracteres):
                    print("Email válido!")
                else:
                    print("Gmail inválido")
                    gm = input("Insira outro Gmail: ")
                    print(f"{n}. {cp}. {gm}")   
print(f"Foi(ram) cadastrado(s) {cadastro} pessoa(s).")
