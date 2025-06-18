from gtp_auto.config.time import is_trade_time
from gtp_auto.analysis.signal import evaluate_price_signal
from gtp_auto.execution.entry import run_entry
from gtp_auto.utils.logger import log

def main():
    log("   ")

    if not is_trade_time():
        log("      -  ")
        return

    log("    ")

    signal = evaluate_price_signal()
    log(f"   : {signal}")

    run_entry(signal)

if __name__ == "__main__":
    main()
