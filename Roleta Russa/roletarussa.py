import random


desc = [0,0,0,0,0,1]
random.shuffle(desc)
tentativas = 0
while desc:
        input("Aperte o Enter para atirar: ")
        resul = desc.pop()

        if resul == 1:
           print("POW!")
           print("Você morreu!")
           break
        else: 
            print("Você tem mais uma tentativa")
            tentativas += 1
            
         

print(f"Teve {tentativas} tentativas")
print("FIM")
