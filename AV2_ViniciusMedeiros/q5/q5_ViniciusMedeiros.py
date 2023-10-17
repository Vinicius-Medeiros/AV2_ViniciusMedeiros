from flask import Flask,request,render_template

app = Flask(__name__, template_folder="templates")
database={'vinicius':'1234','pedro':'@PH321'}

login = lambda : render_template("login.html")

userInDB = lambda : request.form['username'] in database
canLogin = lambda : render_template('login.html',info='Invalid Password') if database[request.form['username']] != request.form['password'] else render_template('home.html',name=request.form['username'])
loginAction = lambda : canLogin() if userInDB() else render_template('login.html',info='Invalid User')

goToRegister = lambda : render_template('register.html')

addUserInDB = lambda : render_template('login.html',info='User registered with success') if database.update({request.form['username']: request.form['password']}) == None else "Algo deu errado..."
registerUser = lambda : addUserInDB() if request.form['username'] not in database else render_template('register.html',info='User already exists')

app.add_url_rule('/', 'login', login)
app.add_url_rule('/form_login', 'form-login', loginAction, methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', goToRegister)
app.add_url_rule('/form_register', 'form-register', registerUser, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8080)