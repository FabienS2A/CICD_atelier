from flask import Flask, jsonify


app = Flask(__name__)




def calcul(x,y):
    a = x
    b = y
    c = (a + b)
    return c

@app.route("/")
def index():
        return jsonify({'hello': 'world'})


if __name__ == '__main__':
      app.run(debug=True)