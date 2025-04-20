from flask import Flask, render_template, request, jsonify
from api.calculator import calculate_dahej

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.form

    result = calculate_dahej(data)

    return render_template('index.html', result=result, form_data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
