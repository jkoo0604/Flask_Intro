from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html', phrase='helloo', times=5)

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    return "Hello, " + name * 2

if __name__ == "__main__":
    app.run(debug=True)