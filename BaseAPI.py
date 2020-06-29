from flask import Flask, jsonify, request
import os
import copy
import socket
import uuid
import json

S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
S.connect(('8.8.8.8', 80))

ExecuteHost = S.getsockname()[0]
#ExecuteHost = 'tayer3simulacion3.tk'

app = Flask(__name__)
emp = [
    {
        "name": 'IBM' , "posi": 3
    },
    {
        "name": 'SaleForce.com' , "posi": 4
    },
    {
        "name": 'SAP' , "posi": 5
    },
    {
        "name": 'Amazon' , "posi": 2
    },
    {
        "name": 'Microsoft' , "posi": 1
    }
]


@app.route("/")
def Hello():
    return {"Message": "Hello!"}


@app.route("/empresas")
def Empress():
    return {
        "data": emp
    }


@app.route("/empdest")
def destacadas():
    for x in (emp):
        print (x)
    return {}


if __name__ == '__main__':
    app.run(debug=True, host=ExecuteHost, port='80')
