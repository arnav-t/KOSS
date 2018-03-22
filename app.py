from flask import Flask, render_template, request
import string as str
import pandas as pd
import numpy as np 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
	if request.method == "POST":
		string = request.form.get('string')
		checked = request.form.get('checkBox')
		data = {'Input':[string], 'Output':[]}
		if(checked):
			string = str.capwords(string)
		else:
			string = string.upper()
		data['Output'].append(string)
		string = r'<script>alert("Result: {}")</script>'.format(string)
		df = pd.DataFrame(data=data)
		with open('./db/hist.csv', 'a') as dbFile:
			df.to_csv(dbFile, header = False, index = False)
		return render_template("home.html", output = string)
	else:
		return render_template("home.html", output = "")
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run()