import json
import requests
import telepot
import pymysql
import socks
import socket
import re


connection = pymysql.connect(
    db='aggregator',
    user='root',
    passwd='1',
    host='localhost')

db = connection.cursor(pymysql.cursors.DictCursor)


def execute():
    poxy_ip()

    public_list = get_public_list()

    for public in public_list:
        url = get_request_url(public['owner_id'])
        text_response = requests.get(url).text
        json_response = json.loads(text_response)

        # filePath = '/Users/Ruslan/PycharmProjects/untitled/cli/telegram_aggregator/response.json'
        # connection_file = open(filePath, encoding='utf-8')
        # json_response = json.load(connection_file)

        post_date = json_response['response']['wall'][1]['date']
        photo_attachments = filter_by_photo_attachment(json_response['response']['wall'][1]['attachments'])
        channel_id = get_channel_id(public)
        public_id = public['id_public']

        if not is_already_posted(public_id, channel_id, post_date) \
                and not is_repost(json_response) \
                and not is_adverb(json_response):
            channel = get_channel_by_id(channel_id)

            if channel is not None and channel['is_active'] > 0:
                bot = telepot.Bot('406220380:AAGiFCUDebSNTE6MVhPlybYL1cBTz0QvujI')

                if photo_attachments.__len__() > 1:
                    media_group = []
                    text = xpath_get(json_response['response']['wall'][1], public['post_text'])
                    caption_used = False

                    for attachment in photo_attachments:

                        caption = xpath_get(attachment[attachment['type']], public['post_text'])

                        if caption is None or len(caption) >= 200 or len(caption) == 0:
                            caption = text

                        if caption_used:
                            caption = ''

                        media = {
                            'type': attachment['type'],
                            'media': xpath_get(attachment, public[attachment['type']]),
                            'caption': caption
                        }

                        if caption:
                            caption_used = True

                        media_group.append(media)

                    try:
                        bot.sendMediaGroup(channel['name'], media_group)
                        tag_posted_post(public_id, channel_id, post_date)

                    except telepot.exception.TelegramError:
                        print('Channel post error')

                else:
                    photo = xpath_get(json_response['response']['wall'][1]['attachments'][0], public['photo'])
                    text = xpath_get(json_response['response']['wall'][1], public['post_text'])
                    vidoe = xpath_get(json_response['response']['wall'][1]['attachments'][0], public['video'])
                    file = xpath_get(json_response['response']['wall'][1]['attachments'][0], public['post_file'])
                    music = xpath_get(json_response['response']['wall'][1]['attachments'][0], public['music'])

                    text = clean_html(text)

                    try:

                        #photo and captured text <=199
                        if len(public['photo']) and photo is not None and text is not None and len(text) <= 199:
                            bot.sendPhoto(channel['name'], photo, text)
                            tag_posted_post(public_id, channel_id, post_date)
                            continue

                        #text and if exist photo
                        if len(text):
                            bot.sendMessage(channel['name'], text)
                            bot.sendPhoto(channel['name'], photo, None, True)
                            tag_posted_post(public_id, channel_id, post_date)

                    except telepot.exception.TelegramError:
                        print('Channel post error')


def tag_posted_post(public_id, channel_id, post_date):
    db.execute(
        "SELECT * FROM post_exucuted WHERE " +
        "id_public = " + str(public_id) + " AND id_channel = " + str(channel_id)
    )
    if db.fetchall().__len__():
        db.execute(
            "UPDATE post_exucuted SET post_date=" + str(post_date) + " WHERE id_public = " +
            str(public_id) + " AND id_channel = " + str(channel_id)
        )
        connection.commit()
    else:
        db.execute(
            "INSERT INTO post_exucuted (id_public, id_channel, post_date)"
            " values(" + str(public_id) + "," + str(channel_id) + "," + str(post_date) + ")"
        )
        connection.commit()


def get_public_list():
    db.execute("SELECT * FROM public, public_data WHERE public.id_public_data = public_data.id_public_data")
    return db.fetchall()


def get_channel_id(public):
    db.execute("SELECT id_channel FROM public_channel WHERE id_public = " + str(public['id_public']))
    channel_id = db.fetchall()
    return channel_id[0]['id_channel']


def is_already_posted(public_id, channel_id, post_date):
    db.execute(
        "SELECT * FROM post_exucuted where id_channel = " + str(channel_id) +
        " AND id_public = " + str(public_id) + " AND post_date >=  " + str(post_date)
    )
    already_posted_posts = db.fetchall()

    return already_posted_posts.__len__() > 0


def is_repost(json_response):
    return 'copy_post_date' in json_response['response']['wall'][1].keys()


def is_adverb(json_response):
    return json_response['response']['wall'][1]['marked_as_ads'] == 1


def get_channel_by_id(channel_id):
    db.execute("SELECT * FROM channel WHERE id_channel = " + str(channel_id) + " AND is_active = 1")
    channel = db.fetchall()

    if channel.__len__():
        return channel[0]

    return None


def get_request_url(owner_id):
    url = 'https://api.vk.com/method/wall.get?' \
          'owner_id=' + owner_id + '&' \
          'domain=&' \
          'offset=1&' \
          'count=1&' \
          'filter=owner&' \
          'extended=1&' \
          'v=4.97&' \
          'access_token=686d71abecb677cfa89dea57c24b483e1192687ce78bbd92b4f6ccf059fda1458af809bdf134d8fe35126'

    return url


def poxy_ip():
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
    socket.socket = socks.socksocket


def clean_html(text):
    text = "\n".join(text.split("<br>"))

    clean_r = re.compile('<.*?>')
    clean_text = re.sub(clean_r, ' ', text)

    return clean_text


def xpath_get(mydict, path):
    elem = mydict
    try:
        for x in path.strip("/").split("/"):
            elem = elem.get(x)
    except:
        pass

    return elem


def filter_by_photo_attachment(attachments):
    photo_attachments = []
    for attachment in attachments:
        if 'photo' in attachment:
            photo_attachments.append(attachment)

    return photo_attachments


execute()
