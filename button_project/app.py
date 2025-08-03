import sqlite3
from datetime import datetime

from flask import Flask, render_template, redirect

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS click_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        clicked_at TEXT
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO click_log (clicked_at) VALUES (?)', (datetime.now().isoformat(),))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
