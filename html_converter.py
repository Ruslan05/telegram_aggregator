import re


def clean_html(text):
    clean_r = re.compile('<.*?>')
    clean_text = re.sub(clean_r, ' ', text)

    return clean_text
