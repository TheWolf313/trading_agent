def generate_signal(model, latest_row, buy_th, sell_th):
    prob = model.predict_proba(latest_row)[0][1]

    if prob > buy_th:
        return "BUY"
    elif prob < sell_th:
        return "SELL"
    else:
        return "HOLD"