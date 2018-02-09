from flask import Flask, render_template, redirect
from instagram.router import instagram_app
from telegram.router import telegram_app
from vk.router import vk_app

app = Flask(__name__)
app.register_blueprint(instagram_app)
app.register_blueprint(vk_app)
app.register_blueprint(telegram_app)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
