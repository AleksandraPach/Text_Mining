import re

html = """<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"""


def znaki_html(string):
    new_html = re.sub('<[^>]+>', '', string)
    return new_html


print(znaki_html(html))
