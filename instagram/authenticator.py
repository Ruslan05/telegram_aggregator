from flask import request, redirect
import config
import requests


def request_code():
    request_url = \
        config.API_PATH_FOR_CODE \
        + 'client_id=' + config.CLIENT_ID \
        + '&redirect_uri=' + config.REDIRECT_URI \
        + '&response_type=' + config.RESPONSE_TYPE

    return redirect(request_url)


def receive_code():
    config.CODE = request.args.get('code')


def request_token():
    response = requests.post(config.API_PATH_FOR_TOKEN, data={
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'grant_type': config.GRAND_TYPE,
        'redirect_uri': config.REDIRECT_URI,
        'code': config.CODE,

    })

    if response.ok:
        config.ACCESS_TOKEN = response.json()['access_token']

    return response

