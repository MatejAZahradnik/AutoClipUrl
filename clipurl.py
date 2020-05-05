import clipboard as clp
from validators import url, domain
import pyshorteners

detected = []
short = {}
s = pyshorteners.Shortener()

def validate(link):
    if url(link) == True:
        return True
    elif domain(link) == True:
        return True
    else:
        return False
while True:
    link = str(clp.paste())
    if not link.endswith('/'):
        link += '/'
    if link not in detected:
        if validate(link):
            print(link)
            detected.append(link)
            if len(link) >27:
                shorter = s.dagd.short(link)
                print(f'shortened to {shorter}')
                short[link] = shorter
        else:
            continue
