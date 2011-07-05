"""
Python CSS Browser Selector v0.0.1
Koes Bong (http://web.koesbong.com)
http://web.koesbong.com/2011/01/28/python-css-browser-selector/
License: http://creativecommons.org/licenses/by/2.5/
Credits: This is a python port from Bastian Allgeier's PHP CSS Browser Selector: http://www.bastian-allgeier.de/css_browser_selector/, 
         which is a port from Rafael Lima's original Javascript CSS Browser Selector: http://rafael.adm.br/css_browser_selector
"""

import re

def get_ua(ua):
    ua = ua.lower()
    g = "gecko"
    w = "webkit"
    s = "safari"
    b = []
    
    # browser
    opera_webtv_matches = re.search(r"opera|webtv", ua)
    opera_matches = re.search(r"opera(\s|\/)(\d+)", ua)
    msie_matches = re.search(r"msie\s(\d)", ua)
    
    if opera_webtv_matches is None and msie_matches is not None:
        b.append("ie ie" + msie_matches.group(1))
    elif ua.find(r"firefox/2") != -1:
        b.append(g + " ff2")
    elif ua.find(r"firefox/4") != -1:
        b.append(g + " ff4")
    elif ua.find(r"firefox/3.6") != -1:
        b.append(g + " ff36")
    elif ua.find(r"firefox/3.5") != -1:
        b.append(g + " ff35")
    elif ua.find(r"firefox/3") != -1:
        b.append(g + " ff3")
    elif ua.find(r"firefox/5") != -1:
        b.append(g + " ff5")
    elif ua.find(r"gecko/") != -1:
        b.append(g)
    elif opera_matches is not None:
        b.append("opera opera" + opera_matches.group(2))
    elif ua.find(r"konquerer") != -1:
        b.append("konquerer")
    elif ua.find(r"chrome") != -1:
        b.append(w + " " + s + " chrome")
    elif ua.find(r"iron") != -1:
        b.append(w + " " + s + " iron")
    elif ua.find(r"applewebkit/") != -1:
        applewebkit_ver_matches = re.search(r"version\/(\d+)", ua)
        if applewebkit_ver_matches is not None:
            b.append(w + " " + s + " " + s + applewebkit_ver_matches.group(1))
        else:
            b.append(w + " " + s)
    elif ua.find(r"mozilla/") != -1:
        b.append(g)
    elif ua.find(r"unknown"):
        b.append("unknown")
    
    #platform
    if ua.find("j2me") != -1:
        b.append("j2me")
    elif ua.find("iphone") != -1:
        b.append("iphone")
    elif ua.find("ipod") != -1:
        b.append("ipod")
    elif ua.find("ipad") != -1:
        b.append("ipad")
    elif ua.find("android") != -1:
        b.append("android")
    elif ua.find("blackberry") != -1:
        b.append("blackberry")
    elif ua.find("mobile") != -1:
        b.append("mobile")
    elif ua.find("mac") != -1 or ua.find('darwin') != -1:
        b.append("mac")
    elif ua.find("webtv") != -1:
        b.append("webtv")
    elif ua.find("win") != -1:
        b.append("win")
    elif ua.find("freebsd") != 1:
        b.append("freebsd")
    elif ua.find("x11") != -1 or ua.find("linux") != -1:
        b.append("linux")
        
    css_selector = {"css": " " . join(b)}
    
    return css_selector
