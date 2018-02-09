from flask import redirect, Blueprint
from .authenticator import request_token


vk_app = Blueprint('vk_app', __name__, template_folder='templates')


@vk_app.route('/auth_vk')
def auth():
    try:
        return request_token()
        # return redirect('/')
    except Exception as exception:
        print(exception)