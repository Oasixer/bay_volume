from settings import Settings
import urllib
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def post_data(url, data, headers={'Content-Type':'application/json'}):
    """
    POST data string to `url`, return page and headers
    """
    params = json.dumps(data).encode('utf8')
    req = urllib.request.Request(url, data=params,
                                 headers=headers)
    return urllib.request.urlopen(req)

def post_to_general(message):
    settings = Settings()
    general = '#temp' # temp TODO update to general when working
    webhook_url = settings.WEBHOOKS['GENERAL']
    data = {
        'text': message,
    }
    response = post_data(webhook_url, data)
    return(None, f'Response: {response}')

def post_to_temp(message):
    temp = '#temp'
    return api_handler('chat.postMessage', text = message, channel = general)

def send_dm(user_id, message):
    return api_handler('chat.postMessage', text = message, channel = user_id)

def get_status(user):
    return api_handler('users.profile.get', user = user)['profile']['status_text']

def set_status(user, text, emoji):
    return api_handler('users.profile.set', user = user, profile = urllib.quote_plus('{"status_emoji":"' + emoji + '","status_text":"' + text + '"}'))

def api_handler(method, text = None, channel = None, user = None, profile = None):
    settings = Settings()
    url = f'https://waterloorocketry.slack.com/api/{method}?token={settings.OAUTH_TOKEN}'
    if channel:
        url += '&channel=' + channel
    if user:
        url += '&user=' + user
    if profile:
        url += '&profile=' + profile
    if text:
        url += '&text=' + urllib.parse.quote_plus(text)
    f = urllib.request.urlopen(url)
    result = f.read().decode('utf-8')
    return json.loads(result)
