from pydub import AudioSegment
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

# 🔥 Force ffmpeg path
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"


# ================= AUDIO → TEXT =================
def audio_to_text(file):
    webm_path = None
    wav_path = None

    try:
        print("📥 Received:", file.filename)

        # Save uploaded audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp:
            temp.write(file.file.read())
            webm_path = temp.name

        print("🎧 Saved:", webm_path)

        # Convert to wav
        audio = AudioSegment.from_file(webm_path, format="webm")
        wav_path = webm_path.replace(".webm", ".wav")
        audio.export(wav_path, format="wav")

        print("🔁 Converted:", wav_path)

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        print("🧠 Recognizing...")

        text = recognizer.recognize_google(audio_data)

        print("✅ RESULT:", text)

        return text

    except Exception as e:
        print("❌ Speech error:", e)
        return None

    finally:
        if webm_path and os.path.exists(webm_path):
            os.remove(webm_path)
        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)


# ================= TEXT → AUDIO =================
def text_to_audio(text: str, language: str = "en-IN"):
    try:
        filename = "reply.mp3"

        lang_code = "ml" if "ml" in language else "en"

        print("🔊 Generating speech in", lang_code)

        tts = gTTS(text=text, lang=lang_code)
        tts.save(filename)

        print("✅ Audio file created:", filename)

        return filename

    except Exception as e:
        print("❌ TTS error:", e)
        return None