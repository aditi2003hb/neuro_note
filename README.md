# 🧠 NeuroNote: The AI-Powered Study Companion

NeuroNote is a smart AI-powered web application built with **FastAPI** and **Hugging Face Transformers** that helps students and learners:

- ✍️ Summarize study content
- 🧾 Generate flashcards
- ❓ Create quiz questions

All from a simple, clean frontend — powered completely by Python 3.13 and usable offline in VS Code.

---

## 🚀 Features

- 📚 AI-generated summaries using NLP
- 🧠 Smart flashcard generation
- 🎯 Quiz questions from your content
- 🌐 FastAPI backend with Swagger docs
- 🎨 Beautiful responsive frontend (HTML/CSS/JS)
- 🔒 Fully local and secure

---

## 🛠️ Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Backend       | FastAPI           |
| AI Models     | Hugging Face Transformers |
| Frontend      | HTML, CSS, JavaScript |
| Styling       | Custom Dark UI    |
| Runtime       | Python 3.13       |

---

## 📁 Folder Structure

```
neuro_note/
│
├── backend/
│   ├── main.py                 # FastAPI app
│   ├── routes/
│   │   └── generate.py         # API endpoint
│   ├── services/
│   │   └── ai_engine.py        # AI logic (summary, quiz, flashcards)
│   └── models/                 # (optional) future database models
│
├── frontend/
│   ├── index.html              # Main frontend page
│   ├── style.css               # Dark theme styling
│   └── script.js               # JS to fetch and display results
│
├── requirements.txt            # Python dependencies
└── README.md                   # You’re here!
```

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/neuro_note.git
cd neuro_note
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI backend
```bash
uvicorn backend.main:app --reload
```

Visit your local API docs at:  
👉 `http://127.0.0.1:8000/docs`

### 4. Run the frontend

Just open the `frontend/index.html` in your browser.

---

## 📋 Sample Input

- **Topic:** "Photosynthesis"
- **Content:** Paste in a few paragraphs from your textbook or PDF.

You’ll get:
- ✍️ A summary
- 🧠 Flashcards
- ❓ Quiz questions (MCQ style or short answer)

---

## 💡 Future Upgrades

- 🔐 User login & history
- 📁 Save/export notes
- 🖨️ Download as PDF
- 📦 Deployment to Render or Railway

---

## 🧑‍💻 Author

**Aditi ([@aditi2003hb](https://github.com/aditi2003hb))**  
Final Year CS Student | Passionate about AI + Dev | Resume-Ready Projects 💼

---

## 🏁 License

MIT License. Free for personal and educational use.
