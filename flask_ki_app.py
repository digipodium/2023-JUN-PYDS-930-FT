from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    data = random.randint(1, 100)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
