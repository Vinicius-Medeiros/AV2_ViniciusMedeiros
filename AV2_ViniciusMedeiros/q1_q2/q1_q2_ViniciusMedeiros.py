# MUDAR O PATH DE ACORDO COM O CAMINHO DO ARQUIVO TEXTO
path = "C:\\Users\\ViniciusMedeiros\\Desktop\\Av2-ProgFunc\\AV2_ViniciusMedeiros\\q1_q2\\q1_q2_ViniciusMedeiros.txt"

openFile = lambda : open(path, "a")
readFile = lambda : open(path, "r")
writeFile = lambda : open(path, "w")
closeFile = lambda file : file.close()

cadastrarUsuario = lambda nL, nS, nSaldo : closeFile(readFile()) if openFile().write(f'{nL}:{nS}:{nSaldo}\n') else print("Nao foi possivel cadastar!")

makeNewListOnlyLogin = lambda l : [padraoLogin(x) for x in l]
identifyPos = lambda l, login : l.index(login)
makeNewListWithoutLogin = lambda l, pos_login : list(filter(lambda x: l.index(x) != pos_login, l))

valorUser = lambda s: s.split(':', 2)[-1] if s.count(':') >= 2 else "Padrão não encontrado na string."
loginEsenha = lambda s: s.split(":", 2)[:2] if s.count(":") >= 2 else s
primeiraPosicao = lambda l : l[0] if len(l) > 0 else 0
padraoLogin = lambda s: s.split(":", 1)[0] if (":" in s) else "Padrão não encontrado na string."

achaValorUser = lambda login, senha : int(primeiraPosicao([valorUser(str(line).strip('[]')) for line in readFile() if login in line])) if fazer_login(login, senha) else -10
fazer_login = lambda login, senha: any(":".join(loginEsenha(line)) == f'{login}:{senha}' for line in readFile())
depositar = lambda login, senha, valorAdepositar: closeFile(readFile()) if openFile().write(f'{login}:{senha}:{valueOnBank + valorAdepositar}\n') else print("Algo deu errado")
sacar = lambda login, senha, valorAsacar, valueOnBank : closeFile(readFile()) if openFile().write(f'{login}:{senha}:{valueOnBank - valorAsacar}\n') else print("Algo deu errado")
possoSacar = lambda login, senha, valorAsacar, valueOnBank : sacar(login, senha, valorAsacar, valueOnBank) if valorAsacar <= valueOnBank else print("\nSaldo Insuficiente\nO seu saldo atual e de R$" + str(valueOnBank))

restart_program = lambda: exec(open(__file__).read())
while True:
    print("\nBem-vindo ao banco")
    print("1 - Cadastrar-se")
    print("2 - Logar")
    print("3 - Sair")

    opcaoInicial = input("Escolha uma opcao: ")
    match opcaoInicial:
        case '1':
            novaUsuario = input("Digite o nome de usuario desejado: ").lower()
            novaSenha = input("Digite a nova senha: ").lower()
            saldo = input("Digite o saldo da sua conta: R$")
            cadastrarUsuario(novaUsuario, novaSenha, saldo)

        case '2':
            break

        case '3':
            print("\nObrigado por visitar!")
            exit()

        case _:
            print("\nOpcao invalida. Tente novamente.\n")

while True:
    login = input("\nDigite o usuario: ")
    senha = input("Digite a senha: ")

    match (fazer_login(login, senha)):
        case True:
            print("\nLogado com sucesso!")
            break
            
        case _:
            print("\nUsuario ou senha incorretos! Tente novamente.")
            descisao = input("Deseja voltar (sim/nao)? ")
            match descisao:
                case 'sim':
                    restart_program()

while True:    
    print("\n1 - Sacar")
    print("2 - Depositar")
    print("3 - Desconectar")
    print("4 - Sair")
    
    opcao = input("Escolha o que deseja fazer: ")
    valueOnBank = achaValorUser(login, senha)
    match opcao:
        case '1':
            valorAserSacado = int(input("Digite o valor que deseja sacar: R$"))
            
            possoSacar(login, senha, valorAserSacado, valueOnBank)
            match ((valorAserSacado <= valueOnBank)):
                case True:
                    print("\nVoce fez um saque no valor de R$" + str(valorAserSacado))
                    print("Seu saldo atual e de R$" + str(valueOnBank - valorAserSacado))
                    lista = [line for line in readFile()]
                    newListWithLog = makeNewListOnlyLogin(lista)
                    loginPos = identifyPos(newListWithLog, login)
                    novaListaSemLoginDesatualizado = makeNewListWithoutLogin(lista, loginPos)
                    with writeFile() as arquivo:
                        arquivo.writelines(novaListaSemLoginDesatualizado)  
        
        case'2':
            valorAserDepositado = int(input("Digite o valor que deseja depositar: R$"))
            depositar(login, senha, valorAserDepositado)
            print("\nVoce fez um deposito no valor de R$" + str(valorAserDepositado))
            print("Seu novo saldo é de R$" + str(valueOnBank + valorAserDepositado))
            lista = [line for line in readFile()]
            newListWithLog = makeNewListOnlyLogin(lista)
            loginPos = identifyPos(newListWithLog, login)
            novaListaSemLoginDesatualizado = makeNewListWithoutLogin(lista, loginPos)
            with writeFile() as arquivo:
                arquivo.writelines(novaListaSemLoginDesatualizado)
        
        case'3':
            print("Deslogando da sua conta...")
            restart_program()

        case'4':
            print("Finalizando a sessao....")
            exit()
        
        case _:
            print("\nOpção invalida. Tente novamente.\n")