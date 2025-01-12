from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__)

LOG_FILE = "./data/activity_log.csv"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logs")
def get_logs():
    """
    Reads the activity log and returns it as JSON for real-time updates.
    """
    if not os.path.exists(LOG_FILE):
        return jsonify([])  # Return empty list if the log file doesn't exist

    logs = []
    with open(LOG_FILE, 'r') as f:
        reader = csv.DictReader(f)
        logs = [row for row in reader]
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
