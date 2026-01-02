# Menu simples - exercícios de lógica

while True:
    print("\n=== MENU ===")
    print("1 - Somar dois números")
    print("2 - Verificar se número é par ou ímpar")
    print("3 - Contar de 1 a 10")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        print("Resultado da soma:", a + b)

    elif opcao == "2":
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")

    elif opcao == "3":
        print("Contando de 1 a 10:")
        for i in range(1, 11):
            print(i)

    elif opcao == "0":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
