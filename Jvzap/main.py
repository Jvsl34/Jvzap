# Site com os scripts: https://cdnjs.com/
# pip install python-socketio flask-socketio simple-websocket
# http://localhost:5000
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins = "*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast = True)

# Criar a nossa 1ª página = 1ª rota
@app.route("/") # decorator
def homepage():
    return render_template("index.html")

# Roda o nosso aplicativo
socketio.run(app, host = "192.168.0.126")

# websocket -> túnel