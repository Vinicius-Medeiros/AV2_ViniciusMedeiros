path = "C:\\Users\\ViniciusMedeiros\\Desktop\\Av2-ProgFunc\\AV2_ViniciusMedeiros\\q2\\q2_ViniciusMedeiros.txt"

openFile = lambda : open(path, "a")
readFile = lambda : open(path, "r")
closeFile = lambda file : file.close()
cadastrar_user = lambda login, password, file : closeFile(file) if file.write(f'{login}:{password}\n') else print("Algo deu errado")
fazer_login = lambda login, password, file: any(line.strip() == f'{login}:{password}' for line in file)

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    match opcao:
        case '1':
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            cadastrar_user(login, senha, openFile())
            print("\nUsuário cadastrado com sucesso!")
        case'2':
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            if fazer_login(login, senha, readFile()):
                print("\nSUCESSO\n")
            else:
                print("\nFRACASSO\n")
        case'3':
            break
        case _:
            print("\nOpção inválida. Tente novamente.\n")
