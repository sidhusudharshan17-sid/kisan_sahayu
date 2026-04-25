from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from weather import predict_spray

from schemas import ChatRequest, ChatResponse
from chatbot_service import get_farming_reply
from voice_service import audio_to_text, text_to_audio

import joblib
crop_model = None

# load crop model


app = FastAPI(title="KrishiMitra Kerala Voice Chatbot Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "KrishiMitra backend running"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    return get_farming_reply(
        message=req.message,
        language=req.language,
        district=req.district,
        crop=req.crop
    )


@app.post("/api/voice-chat", response_model=ChatResponse)
def voice_chat(req: ChatRequest):
    return get_farming_reply(
        message=req.message,
        language=req.language,
        district=req.district,
        crop=req.crop
    )


@app.post("/api/audio-chat")
def audio_chat(file: UploadFile = File(...)):
    text = audio_to_text(file)

    if not text:
        return {
            "reply": "Could not understand audio. Please try again.",
            "language": "unknown",
            "status": "error",
            "transcribed_text": None
        }

    result = get_farming_reply(text)
    result["transcribed_text"] = text

    return result


@app.post("/api/audio-chat-with-reply")
def audio_chat_with_reply(file: UploadFile = File(...)):
    text = audio_to_text(file)

    if not text:
        return {
            "reply": "Could not understand audio. Please try again.",
            "language": "unknown",
            "status": "error",
            "transcribed_text": None,
            "audio_reply_available": False
        }

    result = get_farming_reply(text)

    audio_path = text_to_audio(
        text=result["reply"],
        language=result["language"]
    )

    return {
        "reply": result["reply"],
        "language": result["language"],
        "status": result["status"],
        "transcribed_text": text,
        "audio_reply_available": audio_path is not None
    }


@app.post("/api/text-to-speech")
def text_to_speech_api(req: ChatRequest):
    audio_path = text_to_audio(req.message, req.language)

    if not audio_path:
        return {"status": "error", "message": "Could not generate audio"}

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="reply.mp3"
    )





@app.post("/api/crop-recommend")
def crop_recommend(data: dict):
    crop = data.get("crop", "banana")
    temperature = data.get("temperature", 30)
    humidity = data.get("humidity", 70)

    if temperature > 28 and humidity > 60:
        recommended = "banana"
        reason = "Warm and humid conditions are ideal for banana cultivation"
    else:
        recommended = "rice"
        reason = "Moderate climate is suitable for rice"

    return {
        "recommended_crop": recommended,
        "confidence": 90,
        "reason": reason
    }

@app.get("/api/weather")
def weather_api(city: str = "Kerala"):
    try:
        weather_data, spray_result = predict_spray(city)

        if not weather_data:
            return {"error": "Weather fetch failed"}

        return {
            "location": city,
            "temperature": weather_data["temp"],
            "humidity": weather_data["humidity"],
            "windSpeed": weather_data["wind"],
            "pressure": weather_data["pressure"],
            "clouds": weather_data["clouds"],
            "condition": "Live Data",
            "spray_advice": str(spray_result)
        }

    except Exception as e:
        return {"error": str(e)}
    

@app.post("/api/crop-recommend")
def crop_recommend(data: dict):

    global crop_model

    try:
        # 🔥 Load only when needed
        if crop_model is None:
            crop_model = joblib.load("crop_model.pkl")

        N = data.get("N")
        P = data.get("P")
        K = data.get("K")
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        ph = data.get("ph")
        rainfall = data.get("rainfall")

        sample = [[N, P, K, temperature, humidity, ph, rainfall]]

        prediction = crop_model.predict(sample)[0]

        return {
            "recommended_crop": str(prediction)
        }

    except Exception as e:
        return {"error": str(e)}
    

