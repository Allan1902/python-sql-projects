#Desafio! 'Escreva ''Olá, Mundo''!
código da resolução do exercício: print('Olá, mundo!')

#Desafio! 'Respondendo o usuário - Seja bem vindo, Allan'
código da resolução do exercício: nome = input('Digite seu nome: ')
print('É um prazer te conhecer,' + nome)


#Cria um programa que leia dois números, e faça a soma entre eles
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))


#Faça um programa que leia algo pelo teclado, e mostre na tela seu tipo primitivo, e todas informações possíveis entre eles
n= (input('Digite algo'))
print('É um número?', n.isnumeric())
print('É um alfabetico?', n.isalpha())
print('É um espaço?', n.isspace())
print('Éstá maiúsculo?', n.isupper())
print('Está minusculo?', n.islower())

#Faça operações aritméticas na mesma sintaxe.
n1 = int(input('Digite um número'))
n2 = int(input ('Digite outro número'))
s= n1 + n2
d= n1 / n2
di= n1 // n2
p= n1**n2
sub= n1-n2
print('A soma é {}, a divisão é {: .2f}, a divisão inteira é {}, a potência é {}, a subtração é {},' .format(s, d, di, p, sub))


#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1= int(input('Digite um número'))	
antecessor = n1 - 1
sucessor = n1 + 1
print('Antecessor é , {}, Sucessor é , {}'.format(n1 -1, n1 + 1)) 
OBS: Na resolução foi mostrado uma forma de escrever a sintaxe sem declarar as variáveis, no próximo desafio será realizado nessa maneira.

#Crie um algoritmo que leia um número, mostre seu dobro, o seu triplo e a sua raiz quadrada.
n = int(input('Digite um número: '))
print('Analisando o número digitado o dobro é: {}, \no seu triplo é: {}, \ne a sua raiz quadrada é {: .2f}'.format((n*2), (n*3), (n**(1/2))))	


#Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ((n1 + n2) / 2)
print( 'A média do aluno é {: .1f} '.format(m))


#Escreva um programa que leia um valor em metros e o exiba convertido em mm e cm.
n = float(input('Digite a metragem: '))
mm = (n * 1000)
cm = (n * 100)
print('A metragem digitada convertida corresponde a {}mm' .format(mm))
print('A metragem digitada convertida corresponde a {}cm' .format(cm))


#Faça um programa que leia um número inteiro e mostre  na tela a sua tabuada.
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('{} x {} = {}' .format(n, 1, n*1))
print('{} x {} = {}' .format(n, 2, n*2))
print('{} x {} = {}' .format(n, 3, n*3))
print('{} x {} = {}' .format(n, 4, n*4))
print('{} x {} = {}' .format(n, 5, n*5))
print('{} x {} = {}' .format(n, 6, n*6))
print('{} x {} = {}' .format(n, 7, n*7))
print('{} x {} = {}' .format(n, 8, n*8))
print('{} x {} = {}' .format(n, 9, n*9))
print('{} x {} = {}' .format(n, 10, n*10))
print('-'*12)


#Crie um programa que leia quanto $ a pessoa tem na carteira, e quantos dólares ela consegue comprar. 1 dólar = 3.27 reais.
reais = float(input('Digite o valor que você tem na carteira: '))
print('Baseado na quantidade de reais que você tem na carteira, conseguirá comprar {: .2f} dólares' .format(reais/3.27))























