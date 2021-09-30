from os import name
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/user_form'
db = SQLAlchemy(app)


class form(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    pwd = db.Column(db.String(20), unique=True, nullable=False)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if (request.method=='POST'):
        name = request.form.get('name')
        password = request.form.get('password')

        entry = form(name=name, pwd=password)
        db.session.add(entry)
        db.session.commit()
    return render_template('signup.html')

# @app.route("/register")
# def register():
#     return render_template('')

if __name__ == '__main__':
    app.run(debug=True)