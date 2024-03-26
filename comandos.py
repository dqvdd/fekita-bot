from telebot.apihelper import ApiException

def messages_commands(bot):

    # Comando Start, para saludar al bot
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, "Hola, soy el bot del grupo Exotic.")

    #comando decir, para hacer que el bot diga algo
    @bot.message_handler(commands=["decir"])
    def decir(message):
        decir_message = message.text[6:] if len(message.text) > 6 else None
        if decir_message:
            if message.reply_to_message:
                bot.reply_to(message.reply_to_message, decir_message)
            else:
                bot.send_message(message.chat.id, decir_message)

    # Comando help, para explicar los comandos disponibles
    @bot.message_handler(commands=["help"])
    def help(message):
        help_message = "Los comandos disponibles son:\n/start: Saluda al bot\n/decir: Hace que el bot diga algo\n/afk: Pone tu estado en AFK\n/brb: Pone tu estado en BRB"
        bot.send_message(message.chat.id, help_message)


    ## Comandos de exploit y exploitme
        
    def error_message(e):
        if "user is an administrator of the chat" in str(e):
            return "El usuario es un Administrador"
        elif "can't remove chat owner" in str(e):
            return "No se puede expulsar al Creador del grupo"
        else:
            return str(e)

    @bot.message_handler(commands=['exploit'])
    def kick_user(message):
        try:
            if message.reply_to_message:
                bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        except ApiException as e:
            bot.send_message(message.chat.id, error_message(e))

    @bot.message_handler(commands=['exploitme'])
    def kick_self(message):
        try:
            bot.kick_chat_member(message.chat.id, message.from_user.id)
            bot.unban_chat_member(message.chat.id, message.from_user.id)
        except ApiException as e:
            bot.send_message(message.chat.id, error_message(e))


