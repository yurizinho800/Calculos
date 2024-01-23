
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

print(G + "_            _           _")
print("  ___ __ _| | ___ _   _| | __ _  __| |"") ___  _ __ __ _")
print(" / __/ _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |")
print("| (_| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |")
print(" \___\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|" + W)

def soma(a,b):
 return a + b

def subtracao(a,b):
 return a - b

def multiplicacao (a,b):
 return a * b

def divisao(a,b):
 if b != 0:
    return a / b
 else: 
   return "erro divisao por zero" 

num1 = float(input("digite o primeiro número:"))
num2 = float(input("digite o segundo número:"))

resultado_soma = soma(num1,num2) 
resultado_subtracao = subtracao(num1,num2)
resultado_multiplicacao = multiplicacao(num1,num2)
resultado_divisao = divisao(num1,num2)

print("soma:",resultado_soma)
print("subtracao:",
resultado_subtracao)
print("multiplicacao:",
resultado_multiplicacao)
print("divisão:",resultado_divisao)
