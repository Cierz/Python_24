from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def lucky():
    return render_template('lucky.html')
	
if __name__ == '__main__':
    app.run()