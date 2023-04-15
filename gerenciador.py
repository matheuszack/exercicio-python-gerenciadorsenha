import csv

def adicionar_senha():
    site = input("Digite o nome do site ou serviço: ")
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    with open('senhas.csv', 'a', newline='') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow([site, usuario, senha])
    print("Senha adicionada com sucesso!")

def mostrar_senhas():
    with open('senhas.csv', 'r') as arquivo_csv:
        ler = csv.reader(arquivo_csv)
        for linha in ler:
            print(f"Site: {linha[0]}, Usuário: {linha[1]}, Senha: {linha[2]}")

while True:
    print("1 - Adicionar senha")
    print("2 - Mostrar senhas")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_senha()
    elif opcao == '2':
        mostrar_senhas()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
