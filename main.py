import os
from flask import Flask, render_template, request

#Inicio Flask
app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.route("/", methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('next') == 'next':
            print("logeado")
            os.system("pedir.py")
    #Si el logeo fue correcto, ejecuto:....
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
