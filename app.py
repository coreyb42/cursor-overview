from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Home page with calculator"""
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint for server-side calculations"""
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Safely evaluate the mathematical expression
        # Note: eval is used here for simplicity, but in production,
        # consider using a safer alternative like ast.literal_eval or a math parser
        result = eval(expression, {"__builtins__": {}}, {})
        
        return jsonify({'result': result, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

