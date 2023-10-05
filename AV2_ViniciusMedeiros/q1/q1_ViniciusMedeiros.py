dicUser = {
    'Vinicius Medeiros' : 'senha123',
    'Pedro Henrique' : 'asd321',
    'Joao Lucas' : 'batata33',
}
dicBank = {
    'Vinicius Medeiros' : 150,
    'Joao Lucas' : 0,
    'Pedro Henrique' : 500,
}

updateAuxDep = lambda user, a : { **{ user: dicBank[user] }, **{ user : a + dicBank[user]}} [user]
updateAuxWit = lambda user, a : { **{ user: dicBank[user] }, **{ user : a - dicBank[user]}} [user]

updateBalance = lambda user, value : print('Seu novo saldo e =', updateAuxDep(user, value)) if dicBank[user] > -1 else print('Error!!!')

withdrawAmount = lambda user, amountValue : print('Seu saldo anterior era de', dicBank[user], 'sacando em uma quantia de', amountValue,
'seu novo saldo e =', updateAuxWit(user, amountValue))

deposit = lambda user, amountValue : updateBalance(user, amountValue) if amountValue > 0 else print('Algo deu errado tente novamente.')

withdraw = lambda user, value : print('Saldo insuficiente para sacar essa quantia de', value) if value > dicBank[user] else withdrawAmount(user, value)

checkAcc = lambda user, password, value : withdraw(user, value) if password == 'withdraw' else deposit(user, value)

checkPassword = lambda user, password, action, value : checkAcc(user, action, value) if dicUser[user] == password else print('login ou senha incorreto!')

checkAccLogin = lambda user, password, action, value : checkPassword(user, password, action, value) if user in dicUser.keys() else print('login ou senha incorreto!')

checkAccLogin("ViniciusMedeiros", "senha123", "deposit", 150)
checkAccLogin("Vinicius Medeiros", "senha1234", "deposit", 150)
checkAccLogin("Vinicius Medeiros", "senha123", "deposit", 150)
checkAccLogin("Vinicius Medeiros", "senha123", "withdraw", 150)
checkAccLogin("Vinicius Medeiros", "senha123", "withdraw", 180)
checkAccLogin("Vinicius Medeiros", "senha123", "deposit", 0)