from flask import Flask, render_template, request, jsonify
import sqlite3
from chatbot import get_response

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    conn = sqlite3.connect('chat_logs.db')
    c = conn.cursor()
    # Create a table to store user inputs and bot responses
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user_msg TEXT, bot_reply TEXT)''')
    conn.commit()
    conn.close()

init_db()  # Initialize database when app starts

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botReply = str(get_response(userText))

    # Log the conversation to SQLite
    try:
        conn = sqlite3.connect('chat_logs.db')
        c = conn.cursor()
        c.execute("INSERT INTO logs (user_msg, bot_reply) VALUES (?, ?)", (userText, botReply))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error logging to DB: {e}")

    return botReply

if __name__ == "__main__":
    app.run(debug=True)