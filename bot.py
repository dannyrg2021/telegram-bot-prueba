import telebot
import threading
import time

# 🔥 Tu token de Telegram
TOKEN = "7373395275:AAHWtC-ssrB4GhDGQAiQMk7D41ywNpCrijI"
bot = telebot.TeleBot(TOKEN)

# ID del usuario al que se enviarán mensajes periódicos
CHAT_ID = 1666690040

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

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy un bot de prueba.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Has dicho: {message.text}")

print("Bot corriendo...")
bot.polling()



