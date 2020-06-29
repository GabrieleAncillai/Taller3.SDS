from flask import Flask, jsonify, request
import random
import flask
import os
import copy
import uuid
import socket

S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
S.connect(('8.8.8.8', 80))

ExecuteHost = S.getsockname()[0]

app = Flask(__name__)

Empresas = [
    {
        "name": 'SaleForce.com' , "id": "1"
    },
    {
        "name": 'IBM' , "id": "2"
    },
    {
        "name": 'SAP' , "id": "3"
    },
    {
        "name": 'Amazon' , "id": "4"
    },
    {
        "name": 'Microsoft' , "id": "5"
    }
]


@app.route("/")
def Hello():
    return {"Message": "Hello!"}


@app.route("/CrearEmpresa", methods=['POST']) #C
def CrearEmpresa():
    Enterprise = request.json
    #Enterprise["id"] = uuid.uuid4()
    Enterprise["id"] = str(random.randint(100, 999))
    Empresas.append(Enterprise)
    response = {
        "data": Empresas,
        "message": "Se agregó la empresa!"
    }
    try:
        return response
    except NameError:
        return {
            "message": str(NameError)
        }

    
@app.route("/ListadoEmpresas") #R
def ListadoEmpresas():
    return {
        "data": Empresas
    }

@app.route("/ActualizarEmpresa", methods=['POST']) #U
def ActualizarEmpresa():
    try:
        Enterprise = request.json
        didFind = False
        response = {}

        for x in range(len(Empresas)):
            if (str(Empresas[x].get('id')) == str(Enterprise.get('id'))):
                Empresas[x] = Enterprise # El index en donde se encuentra la empresa, se edita
                didFind = True

        if not didFind:
            response = {
                "message": "No se encontró la empresa :("
            }
        else: 
            response = {
                "data": Empresas,
                "message": "Se ha actualizado :)"
            }
        return response

    except NameError:
        return {
            "message": str(NameError)
        }


    

@app.route("/BorrarEmpresa", methods=['DELETE']) #D
def BorrarEmpresa():
    try:
        Enterprise = request.json
        didFind = False
        response = {}

        for x in range(len(Empresas)):
            if (str(Empresas[x].get('id')) == str(Enterprise.get('id'))):
                Empresas.pop(x) # El index en donde se encuentra la empresa, se borra
                didFind = True

        if not didFind:
            response = {
                "message": "No se encontró la empresa :("
            }
        else: 
            response = {
                "data": Empresas,
                "message": "Se ha borrado xd :)"
            }
        return response

    except NameError:
        return {
            "message": str(NameError)
        }


if __name__ == '__main__':
    app.run(debug=True, host=ExecuteHost, port='80')
