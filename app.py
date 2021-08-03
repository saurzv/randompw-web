from flask import Flask, render_template, request, url_for
from driver import RandomPassword

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def say_hello():
	if request.method == "POST" :
		pw = RandomPassword()
		pw.set_lower(int(request.form['n_lower']))
		pw.set_upper(int(request.form['n_upper']))
		pw.set_digits(int(request.form['n_digits']))
		pw.set_spchars(int(request.form['n_spchars']))
		return render_template('index.html', data=pw.generate())
	else :
		return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)