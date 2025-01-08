
# 💻 Tela de Login Simples

É basicamente uma tela de login muito simplificada. Consiste no usuário por seu Nome, CPF e seu Gmail para cadastro em uma empresa, caso o CPF esteja com um número maior ou menor que o CPF exige o programa irá entrar em um loop de while até que em final a pessoa/usuário ponha o CPF correto (**Poderia ter feito com caracteres, pretendo inserir isso ao programa mais futuramente**). Mesma coisa com o Gmail, se o usuário não por o gmail com o final **'gmail.com'**, o programa entrará em loop caso o mesmo não esteja pondo corretamente. Ao final do programa é dado o print de quantos usuários ao final foram cadastrados.

# ❓ Como funciona?

Para deixar mais explicíto do que a explicação anterior, começamos com um programa para validar se **"gm"** vei ter o **"gmail.com"**, após isso começamos com a pergunta do nome do usuário com tipo não específicado. Logo, pergunto o CPF do user, caso o CPF inserido tenha + ou - caracteres que se pede o CPF normal (11 caracteres) entra em um loop em while até que a pessoa escreva o seu CPF com os 11 caracteres. Após sair desse loop do CPF, entra no Gmail, que caso ao fim da escrita não tenha o **"gmail.com"** entra em loop até a pessoa escrever certo... Logo depois, inicia um contador e um **n2 == 's'** que entra em outro loop, que se o **n2** continuar sendo igual há **'s'** continuará "cadastrando" (porque não se tem um banco para guardar as informações). Ao final mostrará o número de pessoas que foram cadastradas.

>Não contém um Banco de Dados para por ao final o nome de todos os usuários cadastrados. Mas isso se vem com tempo e aprendizado. Obrigado!
