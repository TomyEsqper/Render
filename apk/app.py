from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yes')
def yes():
    return jsonify(message="¡Genial! Nos vemos el 14 de febrero ❤️\n¡Eres la mejor! 💕")

@app.route('/no')
def no():
    new_x = random.uniform(0, 100)
    new_y = random.uniform(0, 100)
    return jsonify(x=new_x, y=new_y)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
