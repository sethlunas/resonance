from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello... World!</h1><br><h2>Resonance</h2><p>Coming soon...</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)