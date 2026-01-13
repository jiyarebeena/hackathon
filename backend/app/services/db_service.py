from app.config.firebase import db
from datetime import datetime

def save_receipt(items, total_co2):
    data = {
        "items": items,
        "total_co2": total_co2,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    db.collection("receipts").add(data)

def get_all_receipts():
    receipts = []
    docs = db.collection("receipts").stream()

    for doc in docs:
        receipts.append(doc.to_dict())

    return receipts
