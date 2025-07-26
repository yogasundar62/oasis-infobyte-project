 Multi-Project Python Portfolio – Oasis Infobyte Internship

Welcome to my **multi-functional Python project collection** created during my internship at **Oasis Infobyte**. These projects demonstrate both beginner and advanced skills in GUI design, voice interaction, real-time communication, and API integration.

  Project Structure

```
oasis-infobyte-project/
├── Task 1 - Voice Assistant/
│   └── voice assistant.py
├── Task 2 - BMI Calculator/
│   └── bmi calculator.py
├── Task 3 - Random Password Generator/
│   └── random password generator.py
├── Task 4 - Weather App/
│   └── weather using js.html
├── Task 5 - Chat Application/
│   ├── chatapplication server.py     # Flask backend
│   └── chatapplication.html          # Frontend interface
└── README.md
```


## Tasks Overview

###  **Task 1 – Voice Assistant**
>  `voice assistant.py`

 A desktop-based voice assistant that uses speech recognition to:
- Greet based on time
- Tell time and date
- Open YouTube
- Tell jokes
- Speak responses aloud

---

###  **Task 2 – BMI Calculator (with Chart)**
> `bmi calculator.py`

 A GUI-based calculator using **Tkinter** that:
- Calculates Body Mass Index
- Categorizes result (Normal, Underweight, etc.)
- Tracks and plots BMI history with `matplotlib`

---

###  **Task 3 – Random Password Generator**
> `random password generator.py`

 Secure password generator with a custom GUI:
- Adjustable length
- Toggle letters, digits, symbols
- Clipboard copy feature

---

###  **Task 4 – Weather Web App**
>  `weather using js.html`

 A simple web-based weather dashboard:
- Fetches real-time weather via **OpenWeatherMap API**
- Shows temperature, status, wind speed
- Displays weather icon dynamically

---

###  **Task 5 – Real-Time Chat Application**
>  `chatapplication server.py` (backend)  
> `chatapplication.html` (frontend)

A live chat platform using:
- Flask + Socket.IO for real-time messaging
- CORS for frontend-backend communication
- Event-based message broadcasting

---

##  How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/oasis-infobyte-project.git
   cd oasis-infobyte-project
## Technologies Used

###  Python
- Core logic for:
  - BMI Calculator
  - Password Generator
  - Voice Assistant
- Libraries used:
  - `speech_recognition` and `pyttsx3` for speech-to-text and text-to-speech
  - `tkinter` for graphical user interfaces
  - `matplotlib` for data visualization
  - `random`, `string`, `pyperclip`, `datetime`, etc.

###  HTML, CSS & JavaScript
- Frontend for:
  - Weather Web App
  - Chat Application
- JavaScript used to:
  - Fetch live data from APIs
  - Dynamically update the UI

### Flask (Python Backend)
- Used in the real-time Chat Application
- `Flask-SocketIO` for real-time communication
- `Flask-CORS` for cross-origin requests

###  APIs & External Services
- [OpenWeatherMap API](https://openweathermap.org/) for live weather data
-  `wikipedia` for summary lookups
-  `pyjokes` for fun one-liner jokes


---

##  Author

**Name**: Yoga Sundar  
**Internship**: Oasis Infobyte – July 2025   
**LinkedIn**: https://www.linkedin.com/in/yoga-sundar-27b252293/  
**Email**: yogasoundar62@gmail.com

> Passionate about Python, problem-solving, and building practical projects.
> Open to internships, collaborations, and learning opportunities.

