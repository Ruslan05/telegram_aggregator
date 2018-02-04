import telepot
import socks
import socket
import json
import requests
import re

#iamarchitect

def cleanhtml(text):
    cleanr = re.compile('<.*?>')
    cleanText = re.sub(cleanr, ' ', text)
    
    return cleanText

socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9050)
socket.socket = socks.socksocket

url = 'https://api.vk.com/method/wall.get?' \
      'owner_id=-98559377&' \
      'domain=&' \
      'offset=1&' \
      'count=1&' \
      'filter=owner&' \
      'extended=1&' \
      'access_token=686d71abecb677cfa89dea57c24b483e1192687ce78bbd92b4f6ccf059fda1458af809bdf134d8fe35126'

textResponse = requests.get(url).text
jsonResponse = json.loads(textResponse)

filePath = '/home/pi/Desktop/architecture_aggretator/latest_post_date2.txt'

latestPostDateFile = open(filePath)
latestPostDate = latestPostDateFile.readline()

if jsonResponse['response']['wall'][1]['date'] > float(latestPostDate):
    if 'copy_post_date' not in jsonResponse['response']['wall'][1].keys():
        photo = jsonResponse['response']['wall'][1]['attachment']['photo']['src_big']
        text = jsonResponse['response']['wall'][1]['text']

        text = cleanhtml(text)

        with open(filePath, 'w') as file:
            file.write(str(jsonResponse['response']['wall'][1]['date']))
            
        bot = telepot.Bot('406220380:AAGiFCUDebSNTE6MVhPlybYL1cBTz0QvujI')
        bot.sendPhoto('@architecture_stories', photo, text)
        
    else:
        print('repost')
else:
    print('Already posted')
