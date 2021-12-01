from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Bye Code!"

@app.route('/hello')
def greating():
	return "Hola"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
	nums_sum = a+b
	return str(nums_sum)
