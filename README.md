Ransomware Detection and Dashboard
This project detects ransomware activities in real time and displays results on a web dashboard. It simulates ransomware behavior (file renaming and encryption) for testing purposes.

Features
Real-time ransomware detection based on file changes (created, deleted, encrypted).
Web-based dashboard to view file activities.
Logging of suspicious activities (e.g., file renaming, creation, deletion).
Simulated ransomware behavior (for testing).
Requirements
Python 3.x
Flask
Cryptography
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Project Structure
arduino
Copy code
ransomware-detection/
├── app/
│   ├── static/
│   ├── templates/
│   └── __init__.py
├── models/
│   └── classifier.pkl
├── data/
│   └── activity_log.csv
├── monitor.py
├── dashboard.py
├── train_model.py
└── requirements.txt
Setup & Run
1. Run the File Monitoring System
The monitor.py script monitors a directory for suspicious file activities.
Start it by running:
bash
Copy code
python monitor.py
2. Start the Web Dashboard
The dashboard.py script runs a Flask server and shows the detected activities.
Run it by:
bash
Copy code
python dashboard.py
Access the dashboard in your browser at http://127.0.0.1:5000/.
Simulate Ransomware (for Testing)
1. Simulate Ransomware
Run the simulate_ransomware.py script to simulate file renaming and encryption.
bash
Copy code
python simulate_ransomware.py
2. Monitor & View Detection
Run monitor.py and dashboard.py to see live detections of file changes and ransomware activity.
Logs
All detected file activities are logged in data/activity_log.csv.
The dashboard dynamically updates using this log.
How It Works
monitor.py: Monitors files for changes (e.g., creation, deletion, encryption).
dashboard.py: Shows real-time logs on a web interface.
simulate_ransomware.py: Simulates ransomware for testing detection.
Technologies Used
Python for file monitoring.
Flask for the dashboard.
Cryptography for simulating ransomware.
CSV for logging file activities.
