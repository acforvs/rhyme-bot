from pyrogram import Client, Message

from static import get_settings
get_settings()
from static import SETTINGS
from rhyme import get_random_rhyme

tg_user = Client('User_Session')

def check_settings(message) -> bool:
    if (message.from_user.username == SETTINGS['OWNER']) is not SETTINGS['DEBUG']:
        return False
    if not SETTINGS['GROUPS']:
        if message.chat.type != 'private':
            return False
    if SETTINGS['IS_TARGET']:
        if message.from_user.username not in SETTINGS['TARGET']:
            return False
    return True

@tg_user.on_message()
def rhyme(client, message) -> Message:
    if not check_settings(message):
        return
    try:
        last_word = message.text.split()[-1]
        print(last_word)
        rhyme_word = get_random_rhyme(last_word)
        tg_user.send_message(message.chat.id, rhyme_word)
    except:
        return

tg_user.run()
tg_user.idle()
