from flask import Flask, render_template, request
import string as str

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
	if request.method == "POST":
		string = request.form.get('string')
		checked = request.form.get('checkBox')
		if(checked):
			string = str.capwords(string)
		else:
			string = string.upper()
		string = r'<script>alert("Result: {}")</script>'.format(string)
		return render_template("home.html", output = string)
	else:
		return render_template("home.html", output = "")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run()