#Faça um programa que leia um número e mostre na tela o dobro deste número, este número elevado ao cubo e a raiz quadrada do número digitado.
import math

x = float(input("Digite um número.\n"))

dobro = x*2
cubo = x**3
if x >= 0:
    raiz = math.sqrt(x)
else:
    raiz = "imaginária, portanto não pertence aos números reais"
txt = "\nO dobro deste número é {}\nEste número elevado à terceira potência é {}\nA raíz quadrada desse número é {}"

print(txt.format(dobro, cubo, raiz))
input("\nPressione ENTER para encerrar.")