# 🤖 CareerMate Chatbot – Career Path Oracle 🧙‍♂️

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Google Gemini](https://img.shields.io/badge/AI%20Model-Google%20Gemini-yellow?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Overview

**CareerMate Chatbot** (also known as *Career Path Oracle*) is an **AI-powered career guidance platform** built with **Streamlit** and **Google Gemini**.  
It analyzes resumes, extracts key skills, and recommends personalized career paths — helping students and professionals make smarter, data-driven career choices.

---

## 🚀 Features

- 📄 **Resume Analyzer** — Upload your resume (PDF/DOCX) and extract skills instantly using Gemini AI.  
- 💬 **AI Chat Assistant** — Ask career-related questions and get contextual answers in real time.  
- 💼 **Career Path Suggestions** — Get tailored, high-paying job roles based on your skills.  
- 📚 **Upskilling Recommendations** — Suggests free learning resources for your career growth.  
- 🎨 **Modern UI** — Built with Streamlit and `streamlit-option-menu` for a smooth, responsive interface.

---

## 🧩 Project Structure

CareerMate-chatbot/
│<br/>
├── app.py # Main Streamlit interface<br/>
├── resume.py # Resume Analyzer logic<br/>
├── assistant.py # Chatbot assistant logic<br/>
├── requirements.txt # Project dependencies<br/>
├── .env # Gemini API key (not uploaded)<br/>
└── README.md # Project documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mohd-ksr/CareerMate-chatbot.git
cd CareerMate-chatbot
```
### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Add your Gemini API Key
Create a file named .env in the project root:<br/>
GEMINI_API_KEY=your-google-gemini-api-key

### 5️⃣ Run the application
```bash
streamlit run app.py
```
---

## 🧠 Tech Stack
| Category          | Tools                                 |
| ----------------- | ------------------------------------- |
| **Frontend/UI**   | Streamlit, Streamlit Option Menu      |
| **AI/NLP**        | Google Gemini (`google-generativeai`) |
| **File Handling** | PyPDF2, python-docx                   |
| **Environment**   | Python-dotenv                         |
| **Visualization** | Graphviz                              |
| **Language**      | Python 3.10+                          |

---

## 📂 Supported File Types
| Type    | Description                                  |
| ------- | -------------------------------------------- |
| `.pdf`  | Extracts readable text from standard resumes |
| `.docx` | Parses text from Word-based resumes          |

---

## 📸 Screenshots

<p align="center">
  <img src="assets/home.png" alt="Home Page" width="400"/>
  <img src="assets/analyzer.png" alt="Resume Analyzer" width="400"/>
</p>

<p align="center">
  <img src="assets/chat.png" alt="Chat Assistant" width="400"/>
  <img src="assets/career.png" alt="Career Suggestions" width="400"/>
</p>

---

## 💡 Future Enhancements
- 📑 Downloadable PDF Report of Career Suggestions
- 🧭 Interactive Career Roadmap Visualization
- 🧠 Memory-based Conversational Assistant
- 🌗 Dark Mode Support

---

## 🧾 License
This project is licensed under the MIT License.
Feel free to fork, modify, and enhance the project.

---

“Choose a career you love, and you will never have to work a day in your life.”



