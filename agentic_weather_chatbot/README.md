# Agentic Weather Assistant Chatbot

A modern, agentic weather assistant chatbot built with [Chainlit](https://chainlit.io/), OpenAI Agents, and Gemini, providing real-time weather information for any city via conversational AI.

---

## 🚀 Features
- **Conversational Weather Assistant**: Ask for the weather in any city and get real-time updates.
- **Agentic LLM Integration**: Uses OpenAI Agents and Gemini models for intelligent, tool-using responses.
- **Streaming Responses**: Enjoy fast, token-by-token streaming answers.
- **Session Management**: Keeps chat history for a seamless experience.
- **Extensible**: Easily add more tools or agents for new capabilities.

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd agentic-weather-chatbot
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   (Requires Python 3.13+)

---

## 🔑 Environment Variables
Create a `.env` file in `src/app/` with the following keys:

```
WEATHER_API_KEY=your_weatherapi_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```
- `WEATHER_API_KEY`: Get from [weatherapi.com](https://www.weatherapi.com/)
- `GEMINI_API_KEY`: Get from your Gemini/Google Cloud console

---

## 🏃 Usage

From the project root, run:
```bash
cd src/app
chainlit run main.py
```
Then open the provided local URL in your browser to chat with the assistant.

---



---

## 🛠️ Technologies Used
- [Chainlit](https://chainlit.io/) (2.5.5+)
- [OpenAI Agents](https://github.com/openai/openai-agents)
- [Gemini LLM](https://ai.google.dev/gemini-api/docs)
- [WeatherAPI](https://www.weatherapi.com/)
- Python 3.13+

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---


## 👤 Author
**Abdullah Shaikh**  
[GitHub](https://github.com/abdullahsheikh01)
