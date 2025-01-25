from flask import Flask
from routes import correct_grammar_route, correct_spelling_route

app = Flask(__name__)

app.register_blueprint(correct_grammar_route)
app.register_blueprint(correct_spelling_route)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
