from flask import Flask, render_template
import twentyfour

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html')
@app.route('/answer/', methods=['POST'])
def handle_data():
	return render_template('answer.html')

if __name__=='__main__':
	app.run(debug=True)