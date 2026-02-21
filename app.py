from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# store moods in memory (temporary)
moods = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    mood = request.form['mood']
    time = datetime.now().strftime("%d %b %Y, %I:%M %p")
    moods.append({"mood": mood, "time": time})
    return redirect(url_for('show_moods'))

@app.route('/moods')
def show_moods():
    return render_template('moods.html', moods=moods)

if __name__ == '__main__':
    app.run(debug=True)
