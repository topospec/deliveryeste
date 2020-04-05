from flask import Flask, render_template, request
from twilio.rest import Client

account_sid = 'AC62820f71bb34cfc5cfd97bd977c7ddc8'
auth_token = '40b45351cfe6ca60a3a246909a019b13'
client = Client(account_sid, auth_token)

app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.route("/", methods=['GET', 'POST'])
def pedir():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('enviar') == 'enviar':
            print("Pedido enviado!")
            if request.form.get('negocio') == 'Topo':
                numero = "5492634665255"
            elif request.form.get('negocio') == 'Perro':
                numero = "5492634795709"
            solicitud = request.form.get('solicitud')
            enviar(solicitud,numero)
    return render_template("pedir.html")

def enviar(mensaje,numero):
    message = client.messages.create(
                              body=str(mensaje), #Variablejjjkkk
                              from_='whatsapp:+14155238886', 
                              to='whatsapp:+'+numero #numero a donde estoy enviando el mensaje
                          )
    print(message.sid)


if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
