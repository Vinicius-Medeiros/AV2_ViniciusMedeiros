from flask import Flask,request,render_template

app = Flask(__name__, template_folder="templates")
database={'vinicius':'1234','ph':'123'}

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/form_login', methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
            return render_template('home.html',name=name1)
        
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/form_register', methods=['POST','GET'])
def registerNewUser():
    usuario=request.form['username']
    senha=request.form['password']
    if usuario not in database:
        database[usuario] = senha
        return render_template('login.html',info='User registered with success')
    else:
        return render_template('register.html',info='User already exists')
        
if __name__ == '__main__':
    app.run()