from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import validate_phone_number, validate_cpf

app = Flask(__name__)
CORS(app) 

@app.post("/")
def receive_data():

    #Valida se é JSON
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Request must be JSON"
        }), 400
    
    data = request.get_json()

    # Valida os dados do body da requisição
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({
            "status": "error", 
            "message": "Email and password are required"
        }), 400
    
    email = data['email']
    password = data['password']

    return jsonify({
        "status": "success",
        "message": f"Email recebido: {email}. Senha recebida: {password}"
    }), 200


@app.post("/verify")
def receive_data_and_verify():

    #Valida se é JSON
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Request must be JSON"
        }), 400
    
    data = request.get_json()

    # Valida os dados do body da requisição
    if not data or 'cpf' not in data or 'phone' not in data:
        return jsonify({
            "status": "error", 
            "message": "CPF and phone number are required"
        }), 400
    
    cpf = data['cpf']
    phone = data['phone']

    if(not validate_phone_number(phone)):

        return jsonify({
            "status": "error",
            "message": "Phone number doest not match the pattern"
        }), 400
    
    if(not validate_cpf(cpf)):
         return jsonify({
            "status": "error",
            "message": "CPF doest not match the pattern"
        }), 400
    
    

    return jsonify({
            "status": "success",
            "message": f"CPF {cpf} and phone number {phone} are correct"
        }), 200