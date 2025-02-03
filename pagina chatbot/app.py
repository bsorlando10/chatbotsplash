from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/')
def home():
    return "¡Hola, este es el servidor de tu chatbot!"

# Ruta para recibir mensajes y enviar respuestas
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # El mensaje del usuario
    print(f"Mensaje recibido: {user_message}")
    
    # Aquí se procesaría el mensaje y se generaría una respuesta
    bot_response = process_message(user_message)
    
    return jsonify({"response": bot_response})
# Función para procesar el mensaje y devolver una respuesta
def process_message(message):
    if "hola" in message.lower():
        return "¡Hola! ¿En qué puedo ayudarte hoy?"
    elif "horarios" in message.lower():
        return "Nuestro horario es de 9:00 AM a 6:00 PM todos los días."
    elif "precios" in message.lower():
        return "Las entradas son: Adulto - $250, Niño - $125."
    elif "ubicación" in message.lower():
        return "Estamos ubicados en Silao, Gto: https://maps.app.goo.gl/BibFafsR9bhdM1PSA y Nuevo Vallarta; https://maps.app.goo.gl/QavyRbDedcxbCUwG7."
    elif "ubicacion" in message.lower():
        return "Estamos ubicados en Silao, Gto: https://maps.app.goo.gl/BibFafsR9bhdM1PSA y Nuevo Vallarta; https://maps.app.goo.gl/QavyRbDedcxbCUwG7."

    elif "promociones" in message.lower():
        return "¡¿PAGASTE LOS TAMALES? Eɴ SPLASH ᴛᴇ ᴄᴏɴsᴇɴᴛɪᴍᴏs ᴄᴏɴ ᴜɴ ғᴇʟɪᴢ Vɪᴀᴊᴇ 2025! SOMOS EL UNICO HOTEL Y PARQUE ACUATICO CON DELFINES DENTRO DE SUS INSTALACIONES, APROVECHA LOS ÚLTIMOS DIAS DE PROMOCIONES CON PRECIO ESPECIAL, RESERVA ESTE 02 Y 03 DE FEBRERO DEL 2025 🎯 Y VIAJA  ANTES DEL 30 JULIO DEL 2025 ᴘᴀʀᴀ 4 Pᴇʀsᴏɴᴀs! Nᴏ ʜᴀʙʀᴀ ᴍᴇᴊᴏʀ ᴏᴘᴏʀᴛᴜɴɪᴅᴀᴅ ᴘᴀʀᴀ ᴘʟᴀɴᴇᴀʀ ᴛᴜ ᴠɪᴀᴊᴇ ᴄᴏɴ ɴᴏsᴏᴛʀᴏs, ʀᴇsᴇʀᴠᴀ ᴛᴜ ᴘᴀᴏ̨ᴜᴇᴛᴇ ᴀʜᴏʀᴀ. 3 ɴᴏᴄʜᴇs: Dᴇ $8670 ᴀ sᴏʟᴏ $3,699, 2 ɴᴏᴄʜᴇs: Dᴇ $5780 ᴀ sᴏʟᴏ $2,699. Aᴘᴀʀᴛᴀ ᴀ́ʜᴏʀᴀ ᴄᴏɴ $699 ᴘᴇsᴏs ʏ ᴀʜᴏʀʀᴀ ᴄᴏᴍᴏ ɴᴜɴᴄᴀ, ᴘᴀɢᴀ ᴇʟ ʀᴇsᴛᴏ ᴇɴ ᴘᴀɢᴏs ᴄᴏᴍᴏᴅᴏs. Aᴘʟɪᴄᴀ ʀᴇsᴛʀɪᴄᴄɪᴏɴᴇs."
    elif "servicios" in message.lower():
        return "Ofrecemos áreas de descanso, toboganes, piscina de olas, y más. ¡Diversión asegurada!"
    elif "contacto" in message.lower():
        return "Puedes llamarnos al +52 477 192 6998 o enviarnos un mensaje a whatsapp."
    elif "gracias" in message.lower():
        return "¡De nada! Si tienes más preguntas, estaré aquí para ayudarte."
    else:
        return "Lo siento, no entendí eso. ¿Puedes reformular tu pregunta?"


if __name__ == '__main__':
    app.run(debug=True)
