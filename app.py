import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.getenv('APP_NAME', 'My Flask App')  # Default if not set
    return render_template('index.html', app_name=app_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)