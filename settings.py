import os

class Settings:
    OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
    WEBHOOKS = {
        'GENERAL': os.environ.get('WEBHOOK_GENERAL')
    }
    ADMIN_USERS = ['US089MP5G']

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Settings, cls).__new__(cls)

        return cls.instance
