from flask import redirect, Blueprint
import telepot

telegram_app = Blueprint('telegram_app', __name__, template_folder='templates')


@telegram_app.route('/auth_tl')
def auth():
    bot = telepot.Bot('406220380:AAGiFCUDebSNTE6MVhPlybYL1cBTz0QvujI')
    bot.sendMessage('@architecture_stories', 'Hey!')

    return 'ok'
