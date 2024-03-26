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

    # Comando Start, para saludar al bot
    @bot.message_handler(commands=["play"])
    def play(message):
        bot.send_message(message.chat.id, "Holanda.")
