def evaluate_basic_signal(market_data: dict) -> bool:
    """
      :   5  2%   True
    ( .    )
    """
    current_price = market_data.get("current_price")
    past_price = market_data.get("price_5min_ago")

    if not current_price or not past_price:
        return False

    change_ratio = (current_price - past_price) / past_price
    return change_ratio >= 0.02
