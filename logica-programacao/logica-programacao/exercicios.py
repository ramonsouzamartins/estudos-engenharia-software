# Exercícios básicos de lógica de programação

# 1. Exibir uma mensagem na tela
print("Olá! Este é um exercício de lógica de programação.")

# 2. Soma de dois números
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = a + b
print("A soma é:", soma)

# 3. Verificar se um número é par ou ímpar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 4. Contador de 1 a 10
print("Contando de 1 a 10:")
for i in range(1, 11):
    print(i)
