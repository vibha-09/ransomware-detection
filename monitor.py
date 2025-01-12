import os
import math
import joblib
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# Load the trained model
model = joblib.load("models/classifier.pkl")

# Entropy calculation
def calculate_entropy(file_path):
    try:
        with open(file_path, 'rb') as f:
            byte_arr = f.read()
        file_size = len(byte_arr)
        if file_size == 0:
            return 0
        freq_dict = {byte: byte_arr.count(byte) for byte in set(byte_arr)}
        entropy = -sum((freq / file_size) * math.log2(freq / file_size) for freq in freq_dict.values())
        return entropy
    except:
        return -1

# Event handler
class RansomwareMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            entropy = calculate_entropy(event.src_path)
            mod_rate = 10  # Example modification rate
            data = pd.DataFrame([[entropy, mod_rate]], columns=["entropy", "modification_rate"])
            is_encrypted = model.predict(data)[0]

            # Log the activity
            timestamp = datetime.now().isoformat()
            with open("data/activity_log.csv", "a") as log:
                log.write(f"{timestamp},{event.src_path},{entropy},{mod_rate},{is_encrypted}\n")

            if is_encrypted:
                print(f"Potential ransomware detected: {event.src_path}")

# Start monitoring
if __name__ == "__main__":
    path = "."  # Change to the directory you want to monitor
    observer = Observer()
    observer.schedule(RansomwareMonitor(), path=path, recursive=True)
    observer.start()
    print("Monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
