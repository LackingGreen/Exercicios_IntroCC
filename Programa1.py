#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

x = int(input("Digite um número inteiro.\n"))

ant, suc = x-1, x+1
txt = "\nO antecessor desse número é {}\nO sucessor desse número é {}"

print(txt.format(ant, suc))
input("\nPressione ENTER para encerrar.")