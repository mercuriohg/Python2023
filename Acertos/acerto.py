from random import randint
desc = randint(1,10)
num = int(input('Insira um número de 1 a 10: '))
while num != desc:
  if num > desc:
    print('Seu chute foi maior que o número')
    print('Você errou!')
  else:
    print('Seu chute foi menor que o número')
    print('Você errou!')
  num = int(input('Insira outro número de 1 a 10: '))
  if num == desc:
    print('Você acertou!')
