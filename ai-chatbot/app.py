from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

app = Flask(__name__)

# Load Gemini key from environment
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message
    )

    ai_reply = response.text

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
