from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
	return "Homepage test!\n"

if __name__ == "__main__":
	app.run()