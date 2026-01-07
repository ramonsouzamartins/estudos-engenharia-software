def calcular_media(nota1, nota2):
    """
    Calcula a média entre duas notas
    """
    return (nota1 + nota2) / 2


# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento
media = calcular_media(nota1, nota2)

# Saída
print("Média final:", media)

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")
