from flask import Flask, request, render_template
from model import load

app = Flask(__name__)

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        age = request.form['age']
        weight = request.form['weight']
        return redirect(url_for('result',
                                age=age,
                                weight=weight))
    return render_template("Home.html")

@app.route('/result', methods=['GET'])
def result():
    age = request.args.get('age')
    weight = request.args.get('weight')
    prediction = load(age, weight)
    return render_template("result.html",
                           prediction=prediction)