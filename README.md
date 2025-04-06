# Hiring-Assistant-chatbot-for-TalentScout
# TalentScout Hiring Chatbot (College Project)

## What's this?

This is a simple chatbot I built for a project. Imagine a company called "TalentScout" that helps tech people find jobs. This chatbot is like a first step – it talks to candidates online to get basic info.

## What it does:

*   **Chats with Candidates:** Has a simple chat screen using Streamlit.
*   **Asks Questions:** Asks for stuff like name, email, phone, experience, location, and what job they want.
*   **Finds out Skills:** Asks the candidate what technologies they know (like Python, React, AWS, etc.).
*   **Asks *Fake* Tech Questions:** Based on the skills mentioned, it shows some *example* technical questions. **Important:** It doesn't use a real AI brain (like GPT) for this part in this version; the questions are pre-written examples in the code.
*   **Remembers Stuff (for a bit):** Keeps track of the conversation while you're using it in one session.
*   **Looks Okay:** Added some colors and styling to make the chat look a bit nicer.
*   **Says Bye:** Has a polite goodbye message.

## Tech Used:

*   **Python:** The main coding language.
*   **Streamlit:** A cool Python library to make web apps easily (this is what creates the chat interface).
*   **No Real AI/LLM:** This version *simulates* the chat flow. It doesn't actually call advanced AI models.

## How to Run It:

1.  **Get the code:** Clone or download this project.
2.  **Open your terminal/command prompt.**
3.  **Go into the project folder:** `cd path/to/this/folder`
4.  **Install Streamlit (if you haven't):**
    ```bash
    pip install streamlit
    ```
5.  **Run the app:**
    ```bash
    streamlit run chatbot_app.py
    ```
6.  It should open in your web browser automatically!

## Cool Things / Future Ideas:

*   Could hook it up to a real AI like GPT to ask smarter questions.
*   Could save the candidate info to a database or file (doesn't do this now!).
*   Make the email/phone number checks better.

## Data Note:

Right now, it **doesn't save any data** permanently. All the info you type in is forgotten when you close the browser tab. This keeps things simple for the project and avoids privacy issues.
