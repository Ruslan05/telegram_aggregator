import socks
import socket
import requests

url = 'https://api.vk.com/method/wall.get?owner_id=-107886736&domain=&offset=1&count=1&filter=owner&extended=1&access_token=686d71abecb677cfa89dea57c24b483e1192687ce78bbd92b4f6ccf059fda1458af809bdf134d8fe35126'
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9151)
socket.socket = socks.socksocket
print(requests.get(url).text)
