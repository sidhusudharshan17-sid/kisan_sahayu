# AI Powered Farming Assistant - Frontend

## 🌾 Project Overview

This is a comprehensive React-based frontend application for an AI-powered farming assistant. The application provides farmers with smart tools for crop management, weather forecasting, disease detection, and personalized recommendations.

## ✨ Features Implemented

### 1. **Home Dashboard** (`/`)
- Overview statistics (total crops, weather alerts, recommendations, diseases detected)
- Quick action cards for navigating to different features
- Current weather summary
- Farming tips section
- Responsive grid layout

### 2. **AI Chatbot** (`/chatbot`)
- Interactive chat interface with real-time messaging
- Message history with timestamps
- Typing indicators
- Quick question suggestions
- Smooth scroll to latest messages
- Mock AI responses (ready to connect to backend)

### 3. **Image Analysis** (`/upload`)
- Drag and drop image upload
- Image preview before analysis
- Two analysis modes:
  - **Disease Detection**: Identifies crop diseases from leaf images
  - **Soil Analysis**: Analyzes soil composition from soil images
- Visual results display with:
  - Disease name, confidence, severity, and treatment
  - Soil type, pH level, nutrient bars (N, P, K)
  - Recommendations

### 4. **Weather Forecast** (`/weather`)
- Location-based weather search
- Current weather display with temperature, humidity, wind speed
- 7-day weather forecast with icons
- Temperature trend chart (using Recharts)
- Smart farming recommendations based on weather conditions

### 5. **Crop Recommendation** (`/crop-recommendation`)
- Comprehensive form for soil and climate data:
  - Nitrogen, Phosphorus, Potassium levels
  - Temperature and humidity
  - Soil pH level
  - Annual rainfall
- AI-powered crop suggestions with:
  - Confidence percentage
  - Crop description
  - Season, water requirement, soil type
  - Visual confidence bars

## 🛠️ Technology Stack

- **React 18** - UI framework
- **TypeScript** - Type safety
- **React Router DOM** - Client-side routing
- **Axios** - HTTP client (ready for backend integration)
- **Recharts** - Data visualization
- **React Icons** - Icon library
- **CSS3** - Custom styling with gradients and animations

## 📁 Project Structure

```
farming-assistant-frontend/
├── src/
│   ├── components/
│   │   ├── Navbar.tsx              # Navigation bar
│   │   └── Navbar.css
│   ├── pages/
│   │   ├── Dashboard.tsx           # Home page
│   │   ├── Dashboard.css
│   │   ├── Chatbot.tsx             # Chatbot page
│   │   ├── Chatbot.css
│   │   ├── ImageUpload.tsx         # Image analysis page
│   │   ├── ImageUpload.css
│   │   ├── Weather.tsx             # Weather page
│   │   ├── Weather.css
│   │   ├── CropRecommendation.tsx  # Crop recommendation page
│   │   └── CropRecommendation.css
│   ├── services/
│   │   └── api.ts                  # API service (mock data)
│   ├── data/
│   │   └── mockData.ts             # Mock data for development
│   ├── types/
│   │   └── index.ts                # TypeScript type definitions
│   ├── App.tsx                     # Main app component with routing
│   ├── App.css                     # Global app styles
│   ├── index.tsx                   # Entry point
│   └── index.css                   # Global CSS reset
├── package.json
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:
```bash
cd farming-assistant-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open your browser and visit:
```
http://localhost:3000
```

## 🎨 UI/UX Highlights

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern Gradient Themes**: Green farming theme with purple weather accents
- **Smooth Animations**: Hover effects, transitions, and loading states
- **User-Friendly Forms**: Input validation, clear labels, and helpful placeholders
- **Visual Feedback**: Loading indicators, success states, and error handling
- **Intuitive Navigation**: Sticky navbar with active page indicators

## 🔌 Backend Integration Guide

The application is built with mock data but is ready for backend integration:

### Step 1: Update API Base URL
In `src/services/api.ts`, uncomment and update:
```typescript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';
```

### Step 2: Replace Mock Functions
Each API function has commented real implementation. For example:
```typescript
// Current (mock):
export const getWeatherData = async (location?: string): Promise<WeatherData> => {
  await simulateDelay();
  return mockWeatherData;
};

// Replace with:
export const getWeatherData = async (location?: string): Promise<WeatherData> => {
  const response = await axios.get(`${API_BASE_URL}/weather?location=${location}`);
  return response.data;
};
```

### Step 3: Add Environment Variables
Create `.env` file:
```
REACT_APP_API_URL=http://your-backend-url/api
```

## 📊 API Endpoints Expected

Your backend team should implement these endpoints:

```
GET    /api/dashboard/stats          - Dashboard statistics
GET    /api/weather                  - Weather data
POST   /api/crop-recommendation      - Get crop recommendations
POST   /api/soil-analysis            - Analyze soil image
POST   /api/disease-detection        - Detect plant disease
POST   /api/chat                     - Send chat message
GET    /api/chat/history             - Get chat history
```

## 🎯 Key Features for Your Team Presentation

1. **Fully Working UI** - All buttons, inputs, and navigation functional
2. **Mock Data System** - Demonstrates full functionality without backend
3. **API Ready** - Clear integration points marked with TODOs
4. **Professional Design** - Modern, clean, and user-friendly interface
5. **Responsive** - Works on all device sizes
6. **Type Safety** - Full TypeScript implementation

## 📱 Screenshots

The application includes 5 main screens:
1. Dashboard with stats and quick actions
2. Interactive chatbot interface
3. Image upload with drag-and-drop
4. Weather forecast with charts
5. Crop recommendation form with results

## 🔧 Available Scripts

```bash
npm start          # Start development server
npm run build      # Build for production
npm test           # Run tests
npm run eject      # Eject from Create React App (not recommended)
```

## 📝 Notes for Backend Team

- All API calls are centralized in `src/services/api.ts`
- TypeScript types are defined in `src/types/index.ts`
- Mock data can be found in `src/data/mockData.ts`
- Each API function has the real implementation commented out
- File uploads use FormData format

## 🎓 Learning Resources

- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs)
- [React Router](https://reactrouter.com)
- [Recharts](https://recharts.org)

## 👨‍💻 Developer

Frontend Developer - Team Member 1

---

**Status**: ✅ Complete and Ready for Backend Integration
