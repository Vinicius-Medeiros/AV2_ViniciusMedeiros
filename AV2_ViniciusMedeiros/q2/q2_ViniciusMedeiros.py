path = "C:\\Users\\ViniciusMedeiros\\Desktop\\Av2-ProgFunc\\AV2_ViniciusMedeiros\\q2\\q2_ViniciusMedeiros.txt"
funcWrite = open(path, "a")
funcRead = open(path, "r")

cadastrar_user = lambda login, password : funcWrite.write(f'{login}:{password}\n')
fazer_login = lambda login, password: any(line.strip() == f'{login}:{password}' for line in funcRead)

while True:
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    match opcao:
        case '1':
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            cadastrar_user(login, senha)
            print("\nUsuário cadastrado com sucesso!\n")
        case'2':
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            if fazer_login(login, senha):
                print("\nSUCESSO\n")
            else:
                print("\nFRACASSO\n")
        case'3':
            break
        case _:
            print("\nOpção inválida. Tente novamente.\n")
