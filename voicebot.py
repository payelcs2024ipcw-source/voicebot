from flask import Flask, request, jsonify
from googletrans import Translator
from gtts import gTTS
import base64
import io

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get uploaded file
    file = request.files['image']  

    # Dummy AI analysis result in English
    english_text = "The soil is good, suitable for growing wheat."

    # Step 1: Translate English → Malayalam
    translator = Translator()
    translated = translator.translate(english_text, dest="ml")  # ml = Malayalam
    malayalam_text = translated.text

    # Step 2: Convert Malayalam text → Speech (gTTS)
    tts = gTTS(malayalam_text, lang="ml")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Step 3: Encode audio as base64
    audio_base64 = base64.b64encode(audio_bytes.read()).decode("utf-8")

    # Step 4: Return JSON response
    return jsonify({
        "local_text": malayalam_text,
        "audio": audio_base64,
        "is_good": True
    })

if __name__ == "__main__":
    app.run(debug=True)
