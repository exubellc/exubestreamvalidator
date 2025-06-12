from flask import Flask, request, jsonify

app = Flask(__name__)

def is_fake_live(stream):
    flags = []

    if not stream.get("has_live_chat", True):
        flags.append("Missing live chat")

    if stream.get("content_id") in stream.get("archived_upload_ids", []):
        flags.append("Rebroadcasted content")

    if stream.get("source_type") != "live_feed":
        flags.append("Non-live source")

    if stream.get("original_upload_time") < stream.get("current_stream_time"):
        flags.append("Previously uploaded content")

    return {
        "status": "Flagged" if flags else "Clean",
        "reasons": flags
    }

@app.route("/validate", methods=["POST"])
def validate_stream():
    try:
        stream_data = request.get_json()
        result = is_fake_live(stream_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "XubeStreamValidator is live."})
