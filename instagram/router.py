from flask import redirect, Blueprint
import authenticator


instagram_app = Blueprint('instagram_app', __name__, template_folder='templates')


@instagram_app.route('/auth')
def auth():
    try:
        return authenticator.request_code()
    except Exception as exception:
        print(exception.message)


@instagram_app.route('/code')
def receive_code():
    try:
        authenticator.receive_code()
        authenticator.request_token()

        return redirect('/')
    except Exception as exception:
        print (exception.message)
