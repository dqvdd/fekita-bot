import time

def afk_commands(bot):
    # Diccionario para almacenar usuarios AFK y sus mensajes
    afk_users = {}

    # Función para detectar AFK
    @bot.message_handler(commands=["afk"])
    def afk(message):
        user_id = message.from_user.id
        afk_users[user_id] = (time.time(), None)
        bot.send_message(message.chat.id, f"{message.from_user.first_name} está AFK.")

    # Función para detectar "brb"
    @bot.message_handler(func=lambda message: message.text.lower().startswith("brb"))
    def brb(message):
        user_id = message.from_user.id
        afk_message = message.text[4:] if len(message.text) > 4 else None
        afk_users[user_id] = (time.time(), afk_message)
        if afk_message:
            bot.send_message(message.chat.id, f"{message.from_user.first_name} está AFK. \nRazón: {afk_message}")
        else:
            bot.send_message(message.chat.id, f"{message.from_user.first_name} está AFK.")

    # Función para calcular el tiempo AFK
    def get_afk_time(user_id):
        if user_id in afk_users:
            return time.time() - afk_users[user_id][0]
        return None

    @bot.message_handler(content_types=['text', 'audio', 'document', 'image', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
    def handle_all(message):
        user_id = message.from_user.id
        if user_id in afk_users:
            # Verifica si el mensaje es una respuesta a un mensaje propio o a otro mensaje
            if message.reply_to_message and (message.reply_to_message.from_user.id == user_id or message.reply_to_message.from_user.id != user_id):
                bot.send_message(message.chat.id, f"{message.from_user.first_name} volvió después de estar AFK durante {format_time(get_afk_time(user_id))}.")
                del afk_users[user_id]

    # Función para responder a menciones
    @bot.message_handler(func=lambda message: message.reply_to_message and message.reply_to_message.from_user.id in afk_users)
    def afk_mention(message):
        user_id = message.reply_to_message.from_user.id
        afk_time, afk_message = afk_users[user_id]
        if afk_time:
            if afk_message:
                bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} está AFK desde hace {format_time(get_afk_time(user_id))}. \nRazón: {afk_message}")
            else:
                bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} está AFK desde hace {format_time(get_afk_time(user_id))}.")

    # Función para formatear el tiempo AFK
    def format_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        
        time_format = []
        if days > 0:
            time_format.append(f"{int(days)}d")
        if hours > 0:
            time_format.append(f"{int(hours)}h")
        if minutes > 0:
            time_format.append(f"{int(minutes)}m")
        if seconds > 0 or not time_format:
            time_format.append(f"{int(seconds)}s")
        
        return ' '.join(time_format)

