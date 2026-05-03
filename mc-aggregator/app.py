from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

def get_servers():
    servers_env = os.getenv("MC_AGGREGATOR_SERVERS", "")
    return [s.strip() for s in servers_env.split(",") if s.strip()]

@app.route("/status")
def status():
    results = []
    for server in get_servers():
        try:
            r = requests.get(f"https://api.mcstatus.io/v2/status/java/{server}", timeout=5)
            results.append(r.json())
        except:
            results.append({"host": server, "online": False})
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)