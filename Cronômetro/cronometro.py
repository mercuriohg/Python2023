from time import sleep
numS = int(input("Informe até quantos segundos o seu cronometro irá: "))
for i in range(1,numS+1):
    sleep(1)
    hora = i//3600
    min = (i%3600)//60
    seg = i%60
    print(f'{hora:.0f}h: {min:.0f}min: {seg}seg')

    