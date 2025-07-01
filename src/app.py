from flask import Flask, jsonify

app = Flask(__name__)
import datetime
import socket


@app.route("/api/v1/info")
def details():
    return jsonify(
        {
            'hostname': socket.gethostname(),
            'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
            'message': 'bruv!!',
            'deployed_on': 'kubernetes'
        }
    )


@app.route("/api/v1/health")
def health():
    return jsonify({"status": "up"}), 200


if __name__ == "__main__":

    app.run(host="0.0.0.0")


# '/api/v1/details'we
# '/api/v1/healthasswwsssawewwww
