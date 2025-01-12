# Ransomware Detection System

This project is a **real-time Ransomware Detection System** that prevents malicious file encryption activities. The system combines **Python** with **Machine Learning** to detect ransomware in real-time and provides a web-based **Dashboard** for monitoring and control.

---

## Features

### Real-Time Detection
- Monitors specified directories for unauthorized file modifications.
- Detects suspicious activities and prevents ransomware encryption.

### Machine Learning Integration
- Classifies file behavior as benign or malicious using a trained ML model.
- Uses file entropy and activity patterns for accurate detection.

### Dashboard
- User-friendly web interface for real-time monitoring.
- Displays logs of suspicious activities and system responses.

### Automated Response
- Terminates malicious processes to stop ransomware execution.
- Backs up original files to prevent data loss.

---

## Usage

1. **Monitoring and Detection**:
   - Run `monitor.py` to start real-time directory monitoring.
   - The system will detect ransomware-like activities and log them.

2. **Dashboard**:
   - Run `dashboard.py` to view the monitoring logs in a user-friendly interface.
   - The dashboard automatically updates with the latest activity logs.

3. **Testing**:
   - Use `simulate_ransomware.py` to simulate ransomware-like behavior in a test directory.

---

## Screenshots

### Dashboard Overview
*Add a screenshot of your real-time monitoring dashboard here.*

### Detection in Action
*Add a screenshot of ransomware detection and logging here.*

---

## Future Enhancements

- Replace the ML model with advanced deep learning models for better detection accuracy.
- Extend monitoring capabilities to support multiple directories.
- Implement email or SMS alerts for real-time user notifications.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any new features or bug fixes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgements

- Inspired by real-world ransomware detection techniques.
- Built using Python, Flask, and scikit-learn.
