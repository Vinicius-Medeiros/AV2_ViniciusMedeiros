import mysql.connector

# Trocar a senha e demais campos baseado na sua conexao com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="Q4_ProgFuncional",
    password="@q4progfuncional1023",
)

cursor = mydb.cursor()
execSQLcmd = lambda cmd: cursor.execute(cmd)
printLista = lambda l : [print(x) for x in l]

createTable = lambda table, attrs : execSQLcmd("CREATE TABLE " + table + " (" + attrs + ");\n")
createDB = lambda dbname : execSQLcmd("CREATE DATABASE " + dbname + ";\n")
dropDB = lambda dbname : execSQLcmd("DROP DATABASE " + dbname + ";\n")
dropTable = lambda dbname : execSQLcmd("DROP TABLE " + dbname + ";\n")
useDB = lambda dbname : execSQLcmd("USE " + dbname + ";\n")
selectFrom = lambda attrs, table, wherecond : execSQLcmd("SELECT " + attrs + " FROM " + table + " WHERE " + wherecond + ";\n")
insertINTO = lambda table, attrs, values : execSQLcmd("INSERT INTO " + table + " (" + attrs + ")" + " VALUES (" + values + ");\n")
deleteFrom = lambda table, columnName, value : execSQLcmd("DELETE FROM " + table + " WHERE " + columnName + " = " + value + " OR " + columnName + " IS NULL;\n")
updateFrom = lambda table, columnName, newValue, id : execSQLcmd("UPDATE " + table + "\n" + "SET " + columnName + " = " + newValue + "\n" + "WHERE id = " + str(id))

"""
-> DESCOMENTAR O COMANDO ABAIXO APENAS QUANDO GERAR ALGUM ERRO INFORMANDO
-> QUE O UM BANCO DE DADOS COM ESSE NOME JA FOI CRIADO
"""
#dropDB("mydb")
createDB("mydb")
useDB("mydb")

"""
-> LEMBRAR QUE O FORMATO DE DATA QUE PRECISA SER FORNECIDO E NO FORMATO "AAAA-MM-DD"
"""
createTable("usuarios", "id INT , name VARCHAR (255) , console VARCHAR (45)")
createTable("jogos", "id INT , name VARCHAR (255), data_lancamento DATE")

insertINTO("usuarios", "id, name, console", "1, 'Vinicius' , 'PlayStation'")
insertINTO("usuarios", "id, name, console", "2, 'Pedro' , 'Xbox'")

insertINTO("jogos", "id, name, data_lancamento", "1, 'Hollow Knight', '2017-02-24'")
insertINTO("jogos", "id, name, data_lancamento", "2, 'Sekiro: Shadows Die Twice', '2019-03-22'")
insertINTO("jogos", "id, name, data_lancamento", "3, 'Grand Theft Auto V', '2013-09-17'")

#deleteFrom("usuarios", "name", "'Pedro'")
#deleteFrom("jogos", "name", "'Sekiro: Shadows Die Twice'")

#updateFrom("usuarios", "console", "'PS5'", 2)
#updateFrom("jogos", "id", "10", 2)

selectFrom("*", "usuarios", "TRUE")
listaDoBanco = cursor.fetchall()
print("\nTabela de Usuarios: ")
printLista(listaDoBanco)

selectFrom("*", "jogos", "TRUE")
listaDoBanco = cursor.fetchall()
print("\n\nTabela de Jogos:")
printLista(listaDoBanco)

dropTable("usuarios")
dropDB("mydb")