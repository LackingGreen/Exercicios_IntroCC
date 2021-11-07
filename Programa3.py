#Faça um programa que leia um número e apresente a sua tabuada.

num = int(input("Insira um número inteiro.\n"))
mult = 1
tab = "{} * {} = {}"

for x in range(1,11):
    res = num * mult
    print(tab.format(num, mult, res))
    mult += 1

input("Pressione ENTER para encerrar.")