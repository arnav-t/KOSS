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

if __name__ == "__main__":
	app.run()