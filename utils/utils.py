import pytz
from datetime import datetime


def get_now_time():
    now = datetime.now(pytz.timezone('Europe/Bratislava'))
    return now.replace(tzinfo=None)