import datetime
from gtp_auto.config.time import is_trade_window_now

def get_kst_time():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=9)

def is_trade_time():
    kst_now = get_kst_time()
    hour = kst_now.hour
    minute = kst_now.minute

    allowed_time_ranges = [
        (7, 50, 8, 10),
        (22, 50, 23, 10),
    ]

    for start_h, start_m, end_h, end_m in allowed_time_ranges:
        start = datetime.time(hour=start_h, minute=start_m)
        end = datetime.time(hour=end_h, minute=end_m)
        now = kst_now.time()
        if start <= now <= end:
            return True
    return False

def main():
    print("")
    now = get_kst_time()
    print(f"KST : {now.strftime('%Y-%m-%d %H:%M:%S')}")

    if not is_trade_window_now():
        print("[GTP]     .")
        return

    if is_trade_time():
        print("   ")
    else:
        print("   ")

if __name__ == "__main__":
    main()

