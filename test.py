import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)

    return cleantext


print(cleanhtml('Эрфуртский собор <br> Эрфурт, Германия <br> <br> Готика'))
