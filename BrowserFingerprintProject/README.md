# Browser Fingerprinting Detection and Prevention System

A standalone cybersecurity tool built with Python and Playwright that launches Google Chrome, monitors browser APIs for fingerprinting attempts, detects suspicious behaviors, blocks or restricts fingerprinting techniques, and generates analytical reports.

## Project Architecture

```
BrowserFingerprintProject/
│
├── main.py              # Main application entry point
├── requirements.txt     # Python dependencies
│
├── detection/           # Fingerprint Detection Module
│   ├── monitor.js       # Injected JS for monitoring sensitive browser APIs
│   └── detector.py      # Python backend to analyze events and classify behaviors
│
├── prevention/          # Fingerprint Prevention Module
│   ├── blocker.js       # Injected JS to block fingerprinting vectors
│   └── spoof.js         # Injected JS to spoof API values and inject noise
│
├── reports/             # Generated reports (HTML, JSON, logs)
│
├── tests/               # Test suites for detection and prevention
│
└── README.md            # Project documentation
```

## Features

- **Chrome Integration**: Direct automation and instrumentation of the installed Google Chrome browser (no extension required).
- **Client-Side Monitoring**: Lightweight JavaScript hooks to inspect API calls in real time (Canvas, WebGL, AudioContext, Navigator, Screen, Fonts, WebRTC, etc.).
- **Detection Engine**: Python-based event analyzer to detect fingerprinting campaigns and anomalous access frequencies.
- **Prevention Engine**: API restriction, gating, and noise-injection techniques to preserve user anonymity without breaking core web functionality.
- **Reporting**: Detailed summary of detected vectors and countermeasures applied.

## Setup and Usage

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the initial test:
   ```bash
   python main.py
   ```
