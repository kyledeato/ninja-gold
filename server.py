from crypt import methods
import random
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key='secret'
@app.route("/")
def index():
    if 'total' in session:
        print('key exist')
    else:
        session['total'] = 0
        session['message']=''
    return render_template("index.html")

@app.route("/process_money", methods=['POST'])
def process_mondey():
    session['message']+=''
    if request.form['input'] == 'farm':
        value = random_num(10,20)
        session['total'] += value
        session['message'] += f'<p> Earned {value} from farm!</p>'
    elif request.form['input'] == 'cave':
        value = random_num(5,10)
        session['total'] += value
        session['message'] += f'<p> Earned {value} from cave!</p>'
    elif request.form['input'] == 'house':
        value = random_num(2,5)
        session['total'] += value
        session['message'] += f'<p> Earned {value} from house!</p>'
    elif request.form['input'] == 'casino':
        value = random_num(1,2)
        if value == 1:
            value = random_num(0,50)
            session['total'] += value
            session['message'] += f'<p> Earned {value} from casino!</p>'
        else: 
            value = random_num(0,50)
            session['total'] -= value
            session['message'] += f'<p> Lost {value} from casino!</p>'
    elif request.form['input'] == 'reset':
        session['total'] = 0
        session['message']=''
    return redirect('/')


def random_num(num1, num2):
    return random.randint(num1,num2)

if __name__=="__main__":
    app.run(debug=True)