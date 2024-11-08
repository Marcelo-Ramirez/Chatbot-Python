from flask import Flask
from flask_cors import CORS
from routes.chatbot import chatbot_bp

# Inicializa la aplicación Flask
app = Flask(__name__)
CORS(app)

# Registra el blueprint de rutas
app.register_blueprint(chatbot_bp)

# Ruta principal de la API
@app.route('/')
def home():
    return "API de Chatbot funcionando correctamente."

if __name__ == '__main__':
    # Ejecuta la aplicación en modo de depuración y escucha en todas las interfaces
    app.run(debug=True, host='0.0.0.0')
