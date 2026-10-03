transactions =[]
def detect_suspicious_activity(transactions, baseline_avg):
    suspicious = []
    for transaction in transactions:
        if transaction > 3 * baseline_avg or transaction > 10000:
            suspicious.append(transaction)
    total = sum(suspicious)
    print("Suspicious transactions:", suspicious)
    print("Total suspicious transaction volume:", total)

