from flask import Flask,render_template,request,flash

app = Flask(__name__)
app.secret_key = "Abandon89_flashing"

@app.route("/")
def index():
    flash("What's your name? ")
    return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")

