import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Components
import Navbar from "./components/Navbar";

// Pages
import Dashboard from "./pages/Dashboard";
import Chatbot from "./pages/Chatbot";
import ImageUpload from "./pages/ImageUpload";
import Weather from "./pages/Weather";
import CropRecommendationPage from "./pages/CropRecommendation";

// 🔥 GLOBAL STATE PROVIDER
import { AppProvider } from "./context/AppContext";

// Styles
import "./App.css";

function App() {
  return (
    <AppProvider>
      <Router>
        <div className="video-container">

          {/* 🎬 BACKGROUND VIDEO */}
          <video autoPlay loop muted playsInline className="background-video">
            <source src="/videos/farm.mp4" type="video/mp4" />
          </video>

          {/* 🌫️ OVERLAY */}
          <div className="overlay"></div>

          {/* 🌐 APP CONTENT */}
          <div className="App">
            <Navbar />

            <main className="main-content">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/chatbot" element={<Chatbot />} />
                <Route path="/upload" element={<ImageUpload />} />
                <Route path="/weather" element={<Weather />} />
                <Route
                  path="/crop-recommendation"
                  element={<CropRecommendationPage />}
                />
              </Routes>
            </main>
          </div>

        </div>
      </Router>
    </AppProvider>
  );
}

export default App;