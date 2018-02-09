import requests


APP_ID = '6340050'
PRIVATE_KEY = 'Xy0DBis4q1UysSp1e8mN'
SERVICE_ACCESS_KEY = 'ce7cfe1fce7cfe1fce7cfe1f81ce1c43cdcce7cce7cfe1f9418136250c8fbdfa79d23e8'
REDIRECT_URI = 'https://oauth.vk.com/blank.html'
RESPONSE_TYPE_TOKEN = 'token'
TOKEN_ACCESS_RIGHTS = ['photos', 'audio', 'video', 'wall', 'friends']
AUTHORIZE_REQUEST_PATH = 'https://oauth.vk.com/authorize?'
ACCESS_TOKEN = ''


def request_token():
    joined_scopes = ','.join(TOKEN_ACCESS_RIGHTS)
    proxies = {
        'http': 'http://93.188.160.146',
    }
    # response = requests.post(AUTHORIZE_REQUEST_PATH, data={
    #     'client_id': APP_ID,
    #     'redirect_uri': REDIRECT_URI,
    #     'scope': joined_scopes
    #
    # }, proxies=proxies)

    response = requests.get(
        'http://www.online-toolz.com/tools/online-privacy-ip-browser-info.php',
        data={},
        proxies=proxies
    )

    if response.ok:
        ACCESS_TOKEN = response.json()['access_token']

    return response.content
