from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin1@db/RockPaperScissors'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)

@app.route('/')
def form():
    return render_template('register.html')

@app.route('/form', methods=['POST'])
def play_form():
    db.create_all()  #create teh database
    username = request.form['username']
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return render_template('form.html',gamer="Abhi")

@app.route('/submit', methods=['POST'])
def submit():
    def compPick():
        return random.randint(0,2)
    game=['Rock','Paper','Scissors']
    comp=game[compPick()]
    user = request.form['choice']
    result = ""+comp+" :: "+user

    if (comp=='Rock' and user=="Paper") or (comp=='Paper' and user=='Scissors') or (comp=='Scissors' and user=='Rock') :
        result = "Welldone!! You won."+"\n\n\n"+"Computer : "+comp+" Vs You : "+user
    elif(comp==user):
        result = "It's a tie."+"\n\n\n"+" Computer : "+comp+" Vs You : "+user
    else:
        result = "You lose."+"\n\n\n"+" Computer : "+comp+" Vs You : "+user+"\nAnother round ?"
    with open('gamelogs.txt', "a+") as file:
        file.write(result + "\n")
    return render_template('result.html', result=result)
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')