import socks
import socket
import requests

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)
socket.socket = socks.socksocket

url = 'https://api.vk.com/method/wall.get?' \
          'owner_id=-38683579&' \
          'domain=&' \
          'offset=2&' \
          'count=1&' \
          'filter=owner&' \
          'extended=1&' \
          'access_token=686d71abecb677cfa89dea57c24b483e1192687ce78bbd92b4f6ccf059fda1458af809bdf134d8fe35126'

response = requests.get(url)
print(response.text)