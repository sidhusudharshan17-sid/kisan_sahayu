# import requests
# import joblib

# API_KEY = "cbae4816b3797581a0a3259fe1b07755"

# model = joblib.load("spray_model.pkl")


# def get_weather(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

#     response = requests.get(url)
#     data = response.json()

#     return {
#         "temp": data["main"]["temp"],
#         "humidity": data["main"]["humidity"],
#         "pressure": data["main"]["pressure"],
#         "wind": data["wind"]["speed"],
#         "clouds": data["clouds"]["all"]
#     }


# def predict_spray(city):

#     d = get_weather(city)

#     sample = [[
#         d["temp"],
#         d["humidity"],
#         d["wind"],
#         d["pressure"],
#         d["clouds"]
#     ]]

#     result = model.predict(sample)[0]

#     return d, result




import requests
import joblib

API_KEY = "cbae4816b3797581a0a3259fe1b07755"

model = joblib.load("spray_model.pkl")


def get_weather(city):
    print("🚀 Calling OpenWeather API...")

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url, timeout=5)

        print("✅ API response received")

        data = response.json()

        print("📊 Data:", data)

        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind": data["wind"]["speed"],
            "clouds": data["clouds"]["all"]
        }

    except Exception as e:
        print("❌ Weather error:", e)
        return None


def predict_spray(city):
    print("🧠 Predict spray started")

    d = get_weather(city)

    if not d:
        return None, "Weather failed"

    print("🔢 Running ML model...")

    sample = [[
        d["temp"],
        d["humidity"],
        d["wind"],
        d["pressure"],
        d["clouds"]
    ]]

    result = model.predict(sample)[0]

    print("✅ Prediction done:", result)

    return d, result