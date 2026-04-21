def place_order(client, symbol, side, order_type, quantity, price=None):
    import logging

    logging.info(f"[MOCK] Placing order: {symbol} {side} {order_type}")

    order = {
        "orderId": "TEST123456",
        "status": "FILLED",
        "executedQty": quantity,
        "avgPrice": price if price else "MARKET"
    }

    logging.info(f"[MOCK RESPONSE]: {order}")
    return order