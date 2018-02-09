
def get_request_url(owner_id):
    url = 'https://api.vk.com/method/wall.get?' \
          'owner_id=' + owner_id + '&' \
          'domain=&' \
          'offset=1&' \
          'count=1&' \
          'filter=owner&' \
          'extended=1&' \
          'access_token=686d71abecb677cfa89dea57c24b483e1192687ce78bbd92b4f6ccf059fda1458af809bdf134d8fe35126'

    return url
