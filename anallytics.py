import csv, os
from datetime import datetime

def log(topic, title):
    os.makedirs("logs", exist_ok=True)
    with open("logs/performance.csv", "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([datetime.utcnow(), topic, title])
