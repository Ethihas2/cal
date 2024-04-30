from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/',methods=["POST"])
def math_operations():
	equation = request.form['text']
	operation = request.form['operation']
	url = 'https://newton.vercel.app/api/v2//'+operation+'/'+equation
	data = requests.get(url).json()
	answer =data['result']

	return render_template("index.html", result = answer, equation = equation)

if __name__ == "__main__":
	app.run()
