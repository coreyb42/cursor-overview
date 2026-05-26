import ast
import operator

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Whitelisted binary and unary operators for the safe arithmetic evaluator.
_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _safe_eval(node):
    """Recursively evaluate a whitelisted AST node tree.

    Allows only numeric literals, binary arithmetic ops, and unary +/-.
    Raises ValueError on any disallowed node.
    """
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Unsupported constant: {node.value!r}")
    # Backwards-compat for Python <3.8 AST (ast.Num)
    if isinstance(node, ast.Num):  # pragma: no cover
        return node.n
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _BIN_OPS:
            raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
        return _BIN_OPS[op_type](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _UNARY_OPS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        return _UNARY_OPS[op_type](_safe_eval(node.operand))
    raise ValueError(f"Unsupported expression element: {type(node).__name__}")


def safe_arithmetic_eval(expression):
    """Parse and evaluate a restricted arithmetic expression string."""
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("Empty expression")
    tree = ast.parse(expression, mode='eval')
    return _safe_eval(tree)


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

        # Evaluate using a restricted AST walker that only permits numeric
        # literals and the arithmetic operators +, -, *, /, //, %, **.
        result = safe_arithmetic_eval(expression)

        return jsonify({'result': result, 'success': True})
    except Exception as e:
        return jsonify({'error': str(e), 'success': False})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

