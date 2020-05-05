"""
author: Matej A. Z
-*- encoding UTF-8 -*-
Url Shortener app written nativly in python
"""

import rumps
from validators import url, domain
import clipboard as clp
import threading
import pyshorteners

class add_config:
    autoshort = False
    icon = "🔗"


def validate(link):
    if url(link) == True:
        return True
    elif domain(link) == True:
        return True
    else:
        return False

"""
def background_checker():
    while True:
        link = str(clp.paste())
        if not link.endswith('/'):
            link += '/'
        if link not in detected:
            if validate(link):
                print(link)
                detected.append(link)
                if len(link) > 27:
                    shorter = s.dagd.short(link)
                    print(f'shortened to {shorter}')
                    short[link] = shorter
            else:
                continue
"""    


class AutoClipUrl(rumps.App):
    def __init__(self):
        """ init of class """
        super(AutoClipUrl, self).__init__(add_config.icon)
        self.menu = ['Shorten', 'AutoShort', 'Share FeedBack', 'Preferences']
        self.s = pyshorteners.Shortener()

    def shorten(self):
        link = clp.paste()
        short = self.s.dadg.short(link)
        clp.copy(link)
        print(f'short from {link} to {short}')

    @rumps.clicked('AutoShort')
    # Auto Shorten And Copy Links In Clipboard
    def autoshort(self, sender):
        sender.state = not sender.state
        add_config.autoshort = not add_config.autoshort

    @rumps.clicked('Shorten')
    # Auto Shorten And Copy URL In Clipboard If Valid
    def shortncopy(self, _):
        print('shortncopy called')
        self.shorten()
        print('shorten')
        pass

    @rumps.clicked('Share FeedBack')
    # Open Browser On Page With Feedback Formular
    def feednack(self, _):
        print('feedback')
        pass

    @rumps.clicked('Preferences')
    # Open Preferneces
    def prefs(self, _):
        print('prefs')
        pass

if __name__ == "__main__":
    AutoClipUrl().run()
