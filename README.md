# 🎙️ Voice Controlled Library System

A **voice-controlled library management system** built using **Python, Streamlit, and Speech Recognition**.

The application allows users to interact with a digital library using voice commands. Users can authenticate themselves, add books, borrow books, return books, and view the current library through a simple web interface.

## 🚀 Live Demo

🔗 **[Try the Voice Controlled Library System](https://jasmine-voice-library.streamlit.app/)**

---

## ✨ Features

* 🔐 **Voice-controlled authentication**
* 🎤 **Browser-based voice input**
* ➕ Add books using voice commands
* 📕 Borrow books using voice commands
* 🔄 Return books using voice commands
* 📚 View books available in the library
* 📊 Display current book status
* 🔒 Logout functionality
* 🌐 Interactive web interface using Streamlit
* 🤖 Speech recognition using Google Speech Recognition
* 💻 Simple and beginner-friendly Python project

---

## 🛠️ Technologies Used

| Technology                   | Purpose                        |
| ---------------------------- | ------------------------------ |
| 🐍 Python                    | Core programming language      |
| 🎈 Streamlit                 | Web application interface      |
| 🎤 SpeechRecognition         | Converts voice input into text |
| 🌐 Google Speech Recognition | Speech-to-text processing      |
| 🔧 GitHub                    | Source code management         |
| ☁️ Streamlit Community Cloud | Application deployment         |

---

## 📂 Project Structure

```text
Voice-controlled-library-system/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### 📄 File Description

**`app.py`**
Main Streamlit application containing the library management logic, voice recognition, authentication, and user interface.

**`requirements.txt`**
Contains the Python dependencies required to run the application.

**`README.md`**
Project documentation and setup instructions.

**`.gitignore`**
Specifies files and folders that should not be uploaded to GitHub.

---

## 🎤 Voice Commands

After successful authentication, users can give commands such as:

```text
Add book Python Programming
```

```text
Borrow book Python Programming
```

```text
Return book Python Programming
```

```text
Show books
```

```text
Logout
```

The application recognizes the command and performs the corresponding library operation.

---

## 🔐 Voice Authentication

The application includes a simple voice authentication system.

When the application starts, the user is asked to provide the password through the microphone.

### 🔑 Demo Password

```text
1234
```

The user can say:

```text
"1234"
```

or

```text
"one two three four"
```

If the password is recognized correctly, access to the library management system is granted.

> **Note:** This authentication system is designed for demonstration and educational purposes and should not be considered a secure production authentication system.

---

## 📚 Library Operations

### ➕ Add a Book

Users can add a book using a voice command.

Example:

```text
Add book Python Programming
```

The book will be added to the library with the status:

```text
Available
```

---

### 📕 Borrow a Book

Users can borrow an available book.

Example:

```text
Borrow book Python Programming
```

The status changes to:

```text
Borrowed
```

---

### 🔄 Return a Book

Users can return a borrowed book.

Example:

```text
Return book Python Programming
```

The status changes back to:

```text
Available
```

---

### 📖 View Books

Users can say:

```text
Show books
```

The application displays the books currently stored in the library along with their availability status.

---

## ⚙️ How It Works

The application follows this process:

```text
        🎤 Browser Microphone
                 ↓
          🎈 Streamlit App
                 ↓
       🎤 Speech Recognition
                 ↓
          📝 Voice → Text
                 ↓
        🔍 Command Detection
                 ↓
       📚 Library Operation
                 ↓
       📊 Updated Book Status
```

---

## 🧠 System Workflow

```text
User
 │
 ▼
Open Web Application
 │
 ▼
Voice Authentication
 │
 ├── ❌ Incorrect Password
 │       ↓
 │   Access Denied
 │
 └── ✅ Correct Password
         ↓
   Library Dashboard
         ↓
    Voice Command
         ↓
 ┌───────┼────────┬─────────┐
 ▼       ▼        ▼         ▼
Add    Borrow    Return    Show
Book    Book      Book     Books
 │       │        │         │
 └───────┴────────┴─────────┘
             ↓
       Updated Library
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Architecture

```text
GitHub Repository
        │
        ▼
Streamlit Community Cloud
        │
        ▼
Python + Streamlit Application
        │
        ▼
Live Web Application
```

### 🔗 Live Application

**https://jasmine-voice-library.streamlit.app/**

---

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Jasmine-shreya3/Voice-controlled-library-system.git
```

### 2. Navigate to the project directory

```bash
cd Voice-controlled-library-system
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## 📦 Requirements

The project uses the following Python packages:

```text
streamlit
SpeechRecognition==3.17.0
```

These dependencies are listed in `requirements.txt`.

---

## 🔒 Data Storage

The current version uses **Streamlit session state** to store library information while the application session is active.

This means the books are stored temporarily during the current session and are not stored permanently in a database.

### Future versions could include:

* 🗄️ MySQL database
* 🗃️ SQLite database
* ☁️ Cloud database
* 👥 Multiple user accounts
* 📚 Permanent book records

---

## 🚀 Future Enhancements

The project can be further improved with:

* 🔐 Secure user authentication
* 🗄️ Permanent database storage
* 👥 Multiple user accounts
* 📚 Book search functionality
* 🔍 Search books by author or category
* 📊 Library statistics dashboard
* 📅 Due-date management
* 🔔 Return-date reminders
* 🧠 Improved natural-language voice commands
* 🌍 Support for multiple languages
* 📱 Improved mobile interface
* 📈 Admin dashboard
* ☁️ Cloud database integration

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how **speech recognition and Python** can be combined with a **web-based interface** to create an interactive library management system.

The project provides a simple example of using voice interaction to perform everyday library operations.

---

## 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python programming
* Functions and conditional logic
* Speech recognition
* Voice-based interaction
* Streamlit application development
* Session state management
* Web application deployment
* Git and GitHub
* Dependency management using `requirements.txt`

---



## 👩‍💻 Author

### Jasmine Shreya P

B.Tech Information Technology Student

🔗 **GitHub:**
https://github.com/Jasmine-shreya3

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub!

---

## 📜 License

This project is created for **educational and demonstration purposes**.
