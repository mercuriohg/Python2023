def alunosCadastro(alunos, aluno): # Função para cadastrar alunos
    alunos.append(aluno)
    
     
def cadastroSistema(alunos): # Main para adicionar os alunos no dict e lista 
    print("============Sistema de Notas=============")
    while True:
        try: 
            quantAlunos = int(input("Quantos alunos existem na sala? "))
            if quantAlunos <= 0:
                print("Valor inválido.")
                continue
            num_id = len(alunos)
            
            for i in range(quantAlunos):
                num_id += 1

                nome_aluno = input("Insira o nome do aluno: ")  
                notas_aluno = []

                for j in range(1,4):
                    nota = float(input(f"Insira a nota {j} do aluno [Os três trimestres]: "))
                    if 0 <= nota <= 10:
                        notas_aluno.append(nota)
                    else:
                        print("Nota inválida.")
                media_aluno = sum(notas_aluno) / 3
                if media_aluno < 7:
                    apr = "Reprovado"
                elif 6 <= media_aluno < 7:
                    apr = "Recuperação"
                else:
                    apr = "Aprovado"
                    
                aluno = {
                    "id": num_id,
                    "nome": nome_aluno,
                    "notas": notas_aluno,
                    "media": media_aluno,
                    "situacao" : apr
                }   
                
                
                alunosCadastro(alunos, aluno)
                
            print("Aluno(os) cadastrado(os)...")
            break
            
        except ValueError:
            print("Valor inválido. Tente novamente.")
def listarAluno(alunos):
    print("=======Lista de alunos=======")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in alunos:
            print(a)
def buscaPorNome(alunos):
    nome_busca = input("Digite o nome do aluno para buscar: ").strip().lower()
    encontrado = False

    for aluno in alunos:
        if aluno["nome"].lower() == nome_busca:
            print("Aluno encontrado:")
            print(aluno)
            encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")
def removerAluno(alunos):
    try:
        nome_remover = str(input("Digite o nome de quem deseja remover: ")).strip().lower()
        encontrado = True
        for i, aluno in enumerate(alunos):
            if aluno["nome"].lower() == nome_remover:
                alunos.pop(i)
                removido = True
                print("Aluno removido com sucesso!")
                break

        if not encontrado:
            print("Aluno não encontrado.")
            return
        # Reorganiza os id's em ordem
        for idx, aluno in enumerate(alunos, start=1):
            aluno["id"] = idx
    except ValueError:
        print('O resultado esperado é uma [string]')
def main():
    alunos = []
    while True:
     try:
        print("""=========Menu=========
1-Cadastrar
2-Listar
3-Buscar por nome
4-Remover
5-Sair""")
        menu = int(input("Escolha a ação: "))
        if menu < 1 or  menu > 5:
            print("Não existe no menu")
            continue
        if menu == 1:
            cadastroSistema(alunos)
        elif menu == 2:
            listarAluno(alunos)
        elif menu == 3:
            buscaPorNome(alunos)
        elif menu == 4:
            removerAluno(alunos)
        elif menu == 5:
            print("Saindo do Sistema...")
            break       
     except ValueError:
        print("Valor errado.")


if __name__ == "__main__": # Chamando o Main para rodar o código
    main()
