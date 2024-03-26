from telebot import TeleBot
import comandos, afk

# Reemplazar con el token de acceso
bot = TeleBot("6860570837:AAG8-_OXoUJR90fD2fjZBvj9DqQ9skBS9pQ")

# Importa los comandos de los otros archivos
comandos.messages_commands(bot)
afk.afk_commands(bot)

# Inicia el bot
bot.polling()
