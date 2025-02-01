import requests
import json
from flask import Blueprint, request, jsonify
from config import Config

deepseek_bp = Blueprint("deepseek", __name__)

@deepseek_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    payload = {
        "model": Config.DEEPSEEK_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(Config.DEEPSEEK_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return jsonify({"response": result.get("response", "")})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
