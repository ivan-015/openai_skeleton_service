import os
import requests
import json

from flask import Flask, request, abort
from flask_cors import CORS


app = Flask(__name__)


@app.route("/ask_openai", methods=["POST"])
def ask_openai():
    try:

        body = request.json
        prompt = body["prompt"]

        # TODO: Place your OpenAI Token here
        openai_token = ""

        openai_url = "https://api.openai.com/v1/chat/completions"

        # Setting up headers to make OpenAI Request
        headers = {
            "Authorization": f"Bearer {openai_token}",
            "Content-Type": "application/json"
        }

        # Setting up body for request
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(openai_url, headers=headers, data=json.dumps(data))

    except Exception as e:
        abort(500, description="Failed to make OpenAI request")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
