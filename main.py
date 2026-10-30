
from flask import Flask, jsonify, request
from prometheus_client import Counter, Gauge, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from datetime import datetime
import os
import hmac

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)

APP_UPTIME = Gauge(
    "app_status",
    "Application running status"
)

START_TIME = datetime.now()
APP_UPTIME.set(1)

METRICS_TOKEN = os.environ.get("METRICS_TOKEN", "")


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        "application": "CloudMonitor",
        "message": "Cloud application is running!",
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudMonitor"
    }), 200


@app.route("/metrics")
def metrics():
    if not METRICS_TOKEN:
        return jsonify({"error": "Metrics authentication not configured"}), 503

    auth_header = request.headers.get("Authorization", "")
    expected = "Bearer " + METRICS_TOKEN

    if not hmac.compare_digest(auth_header, expected):
        return jsonify({"error": "Unauthorized"}), 401

    REQUEST_COUNT.inc()
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


@app.route("/info")
def info():
    return jsonify({
        "application": "CloudMonitor",
        "uptime_seconds": (
            datetime.now() - START_TIME
        ).total_seconds(),
        "status": "running"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
