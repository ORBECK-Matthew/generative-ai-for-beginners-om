# Prompt : Analyze the code, find weaknesses or gaps (security, structure, readability), then rewrite an improved version.
from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Greets the user by name, using a query parameter.
    Example: /?name=Alice
    """
    name = request.args.get('name', 'World')
    safe_name = escape(name)  # Prevent XSS by escaping input
    return f'Hello, {safe_name}!'

if __name__ == '__main__':
    # Use host='0.0.0.0' for external access, debug=False for production
    app.run(host='127.0.0.1', port=5000, debug=True)