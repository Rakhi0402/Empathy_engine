import os
os.environ["TRANSFORMERS_NO_AUTO_CONVERSION"] = "1"
os.environ["HF_TOKEN"] = "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"  

# then import your emotion detector / transformers stuff
from flask import Flask, request, jsonify, render_template, send_file
from emotion_detector import detect_emotion
from voice_mapper import map_emotion_to_voice
from tts_engine import generate_audio

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/speak", methods=["POST"])
def speak():

    data = request.json
    text = data["text"]

    emotion, confidence = detect_emotion(text)

    rate, volume = map_emotion_to_voice(emotion, confidence)

    audio_file = generate_audio(text)

    response = {
        "emotion": emotion,
        "confidence": float(confidence),
        "rate": rate,
        "volume": volume,
        "audio": audio_file
    }

    return jsonify(response)


@app.route("/audio")
def audio():
    return send_file("output.mp3")


if __name__ == "__main__":
    app.run(debug=True)