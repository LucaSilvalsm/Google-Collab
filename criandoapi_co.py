# -*- coding: utf-8 -*-
"""CriandoAPI-Co.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Gz1j4DaUSbzMFuJSgj22Exf4JVPiuWj
"""

!pip install pyngrok
from pyngrok import ngrok
ngrok.set_auth_token("2i5B88zRq7Q0c1hsCA7l4j7vq2T_3BtZvu3GXNX2Fk1uYctse") # -> Go to 'https://www.ngrok.com/' to create your account and get your Token

from flask import request, jsonify, Flask
import random as rk
import os
import threading

spreadsheet = [
    {
        "Number": "1",
        "Name": "Mahesh",
        "Age": "25",
        "City": "Bangalore",
        "Country": "India"
    },
    {
        "Number": "2",
        "Name": "Alex",
        "Age": "26",
        "City": "London",
        "Country": "England"
    },
    {
        "Number": "3",
        "Name": "David",
        "Age": "27",
        "City": "San Francisco",
        "Country": "USA"
    },
    {
        "Number": "4",
        "Name": "John",
        "Age": "28",
        "City": "Toronto",
        "Country": "Canada"
    },
    {
        "Number": "5",
        "Name": "Chris",
        "Age": "29",
        "City": "Paris",
        "Country": "France"
    }
]

from flask import Flask, jsonify
from pyngrok import ngrok

app = Flask(__name__)
port = 5000

NGROK_AUTH_TOKEN = "2i5B88zRq7Q0c1hsCA7l4j7vq2T_3BtZvu3GXNX2Fk1uYctse"  # Substitua pelo seu token de autenticação ngrok

ngrok.set_auth_token(NGROK_AUTH_TOKEN)  # Configura o token de autenticação ngrok

# Abre um túnel ngrok para o servidor HTTP na porta especificada
public_url = ngrok.connect(port).public_url
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

# Atualiza quaisquer URLs base para usar a URL pública ngrok
app.config["BASE_URL"] = public_url

@app.route("/")
def home():
    return jsonify(spreadsheet)

@app.route("/index")
def input():
    return jsonify({"message": "Hello, world!"})

# Inicia o servidor Flask diretamente (não em um thread separado)
if __name__ == "__main__":
    app.run(use_reloader=False)

"""para visualizar: https://fdff-35-237-38-164.ngrok-free.app/"""