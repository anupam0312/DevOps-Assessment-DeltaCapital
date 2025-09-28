from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify([
        {"id": 1, "name": "Client A"},
        {"id": 2, "name": "Client B"}
    ])

@app.route("/healthz", methods=["GET"])
def health_check():
    return {"status": "ok", "service": "clients-api"}

@app.route("/")
def home():
    return {"message": "Clients API is running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
