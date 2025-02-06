import os
import telebot
from flask import Flask, request
import threading
import time

# 🔥 Tu token de Telegram
TOKEN = "7373395275:AAHWtC-ssrB4GhDGQAiQMk7D41ywNpCrijI"
bot = telebot.TeleBot(TOKEN)

# ID del usuario al que se enviarán mensajes periódicos
CHAT_ID = 1666690040

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot de Telegram activo en Render 🚀"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    update = request.get_json()
    if update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return "OK", 200

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy un bot de prueba desplegado en Render.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Has dicho: {message.text}")

# Función para enviar mensajes cada 30 segundos
def keep_alive():
    while True:
        try:
            bot.send_message(CHAT_ID, "Manteniendo el bot activo en Render 🚀")
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")
        time.sleep(30)  # Espera 30 segundos antes de enviar el siguiente mensaje

# Inicia el proceso en segundo plano
threading.Thread(target=keep_alive, daemon=True).start()

if __name__ == "__main__":
    # Render necesita que la app escuche en un puerto
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
