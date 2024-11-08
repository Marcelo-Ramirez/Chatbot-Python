from flask import Blueprint, request, jsonify
from service.chatbot import get_chatbot_response

# Crea un Blueprint para el chatbot
chatbot_bp = Blueprint('chatbot_bp', __name__)

# Define una ruta para recibir el input del chatbot
@chatbot_bp.route('/message', methods=['POST'])
def chatbot_message():
    data = request.json  # Se espera que el input venga en formato JSON
    user_input = data.get("message")
    
    # Obtén la respuesta del chatbot
    response = get_chatbot_response(user_input)
    
    return jsonify({"response": response})
