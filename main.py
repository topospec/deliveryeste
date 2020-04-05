from flask import Flask, render_template, request
from twilio.rest import Client

#Agrego para facebook login
from flask import url_for, request, session, redirect
from flask_oauth import OAuth
#Fin dependencias facebook

#Credenciales Twilio
account_sid = 'AC62820f71bb34cfc5cfd97bd977c7ddc8'
auth_token = '40b45351cfe6ca60a3a246909a019b13'
client = Client(account_sid, auth_token)

#Credenciales Facebook
FACEBOOK_APP_ID = '000000000000000'
FACEBOOK_APP_SECRET = '0a0b0c00000000000000000000x0y0z0'
oauth = OAuth()

#Inicio Flask
app = Flask(__name__)
PORT = 5000
DEBUG = False

#Inicio sesion en facebook
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

#Obtengo el token
@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

    def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))

#Fin del login con facebook


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
