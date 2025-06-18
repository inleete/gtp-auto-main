import datetime

ALLOWED_TIME_WINDOWS = [
    (7, 50, 8, 10),
    (22, 50, 23, 10),
]

def get_kst_now():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=9)

def is_trade_window_now():
    now = get_kst_now().time()

    for start_h, start_m, end_h, end_m in ALLOWED_TIME_WINDOWS:
        start = datetime.time(hour=start_h, minute=start_m)
        end = datetime.time(hour=end_h, minute=end_m)
        if start <= now <= end:
            return True
    return False
