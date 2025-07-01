from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import datetime
import socket

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # <-- Add this line to enable /metrics

@app.route("/api/v1/info")
def details():
    return jsonify(
        {
            'hostname': socket.gethostname(),
            'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
            'message': 'bruv!!',
            'deployed_on': 'kubernetes'
        }
    )

@app.route("/api/v1/health")
def health():
    return jsonify({"status": "up"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
###ssssddssssss
