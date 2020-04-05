from flask import Flask, render_template, request

#Inicio Flask
app = Flask(__name__)
PORT = 5000
DEBUG = False


@app.route("/", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
