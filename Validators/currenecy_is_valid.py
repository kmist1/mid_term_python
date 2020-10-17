import urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context


def page_exists(page):
    try:
        urllib.request.urlopen(page)
        return True
    except:
        return False
