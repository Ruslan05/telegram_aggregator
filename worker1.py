import json
import requests
import telepot
from cli.telegram_aggregator.poxy import poxy_ip
from cli.telegram_aggregator.html_converter import clean_html
from cli.telegram_aggregator.request_builder import get_request_url
from cli.telegram_aggregator.db_manager import get_db_connection

db = get_db_connection()


def execute():
    poxy_ip()

    public_list = get_public_list()

    for public in public_list:
        url = get_request_url(public['owner_id'])
        textResponse = requests.get(url).text
        jsonResponse = json.loads(textResponse)

        post_date = jsonResponse['response']['wall'][1]['date']
        channel_id = get_channel_id(public)
        public_id = public['id_public']

        if not is_already_posted(public_id, channel_id, post_date):
            if not is_repost(jsonResponse):
                channel = get_channel_by_id(channel_id)

                photo = jsonResponse[public['picture']]
                text = jsonResponse[public['post_text']]
                vidoe = jsonResponse[public['video']]
                file = jsonResponse[public['post_file']]
                music = jsonResponse[public['music']]

                text = clean_html(text)

                bot = telepot.Bot('406220380:AAGiFCUDebSNTE6MVhPlybYL1cBTz0QvujI')
                bot.sendPhoto(channel['name'], photo, text)

                db.execute(
                    "INSERT INTO post_exucuted (id_public, id_channel, post_date)"
                    " values(" + public_id + "," + channel_id + "," + post_date + ")"
                )

            else:
                print('repost')


def get_public_list():
    db.execute("SELECT * FROM public, public_data WHERE id_public = id_public_data")
    return db.fetchall()


def get_channel_id(public):
    db.execute("SELECT id_channel FROM public_channel WHERE id_public = " + public['id_public'])
    channel_id = db.fetchall()
    return channel_id[0]['id_channel']


def is_already_posted(public_id, channel_id, post_date):
    db.execute(
        "SELECT * FROM post_exucuted where id_channel = " + channel_id +
        " AND id_public = " + public_id + " AND post_date >=  " + post_date
    )
    already_posted_posts = db.fetchall()

    return already_posted_posts.count() != 0


def is_repost(jsonResponse):
    return  'copy_post_date' not in jsonResponse['response']['wall'][1].keys()


def get_channel_by_id(channel_id):
    db.execute("SELECT * FROM channel WHERE id_channel = " + channel_id)
    channel = db.fetchall()
    return channel[0]


execute()