from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == "your_verify_token":
        return challenge
    return "Verification failed", 403

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print(data)  # Debugging
    return "Message received", 200

if __name__ == "__main__":
    app.run(port=5000)