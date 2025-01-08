import math

def soma(a,b):
    return a + b    

def divisao(a,b):
    return a / b

def mult(a,b):
    return a * b 

def sub(a,b):
    return a - b 

def raizquadrada(a):
    return math.sqrt(a) 

def sin(a):
    return math.sin(a) 

def cos(a):
    return math.acos(a) 

def tg(a):
    return math.tan(a) 

def titulo(msg):
    tam = len(msg)
    print('=+=' * tam)
    print(  msg)
    print('=+=' * tam)
