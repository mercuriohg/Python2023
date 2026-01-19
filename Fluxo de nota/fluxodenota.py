def alunosCadastro(alunos, aluno): # Função para cadastrar alunos
    alunos.append(aluno)
    
     
    
def main(): # Main para adicionar os alunos no dict e lista 
    while True:
        try: 
            quantAlunos = int(input("Quantos alunos existem na sala? "))
            alunos = []
            num_id = 0
            
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
                elif 6 <= media_aluno <= 6.9:
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
            print("============Lista de Alunos============")
            for a in alunos:
               print(a)

            break
        except ValueError:
            print("Valor inválido. Tente novamente.")

if __name__ == "__main__": # Chamando o Main para rodar o código
    main()
