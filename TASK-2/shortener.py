
import hashlib
from db import save_url, get_long_url, short_exists

def shorten_url(long_url):
    short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]
    if not short_exists(short_code):
        save_url(long_url, short_code)
    return short_code

def retrieve_url(short_code):
    return get_long_url(short_code)
