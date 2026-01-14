import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/readings.csv")

def log_data(temp, humidity):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), temp, humidity])
