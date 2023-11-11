from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output", methods=['POST'])
def output():
    firstValue = float(request.form.get("value_a"))
    action = str(request.form.get("action"))
    secondValue = float(request.form.get("value_b"))
    match action:
        case '+':
            data = firstValue + secondValue
        case '-':
            data = firstValue - secondValue
        case '*':
            data = firstValue * secondValue
        case '/':
            data = firstValue / secondValue
    print(data)
    print(type(data))
    return render_template("output.html", data=data)

app.run(port=8080)