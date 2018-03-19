from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
	if request.method == "POST":
		string = request.form.get('string')
		string = r'<script>alert("Result: {}")</script>'.format(string.upper())
		return render_template("home.html", output = string)
	else:
		return render_template("home.html", output = "")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run()