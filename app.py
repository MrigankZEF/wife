from flask import Flask, render_template, request, redirect, url_for, session
import os
import json
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Load greeting messages
morning_greetings = [
    "Good morning, Mili 🌻",
    "Rise and shine, Mili! ☀️",
    "Morning, Mili! Have a beautiful day 💖",
    "Hey Mili, you're amazing! 🌟",
    "Hi Mili, keep smiling 😊",
    "Good morning, sunshine! 🌞",
    "Hello, Mili! Ready to conquer the day? 💪",
    "Morning, Mili! You light up the world 🌈",
    "Good morning, Mili! Stay awesome ✨",
    "Hi Mili, today is your day! 🌟"
]

afternoon_greetings = [
    "Good afternoon, Mili 🌻",
    "Hello, Mili! Hope your day is going great 💖",
    "Hey Mili, you're doing amazing! 🌟",
    "Hi Mili, keep up the great work 😊",
    "Good afternoon, sunshine! 🌞",
    "Hello, Mili! Keep shining bright 💪",
    "Afternoon, Mili! You inspire the world 🌈",
    "Good afternoon, Mili! Stay wonderful ✨",
    "Hi Mili, keep rocking the day! 🌟",
    "Hello, Mili! You're unstoppable 💖"
]

night_greetings = [
    "Good evening, Mili 🌻",
    "Hello, Mili! Hope you had a great day 💖",
    "Hey Mili, you're amazing! 🌟",
    "Hi Mili, relax and unwind 😊",
    "Good evening, sunshine! 🌞",
    "Hello, Mili! You did great today 💪",
    "Evening, Mili! You light up the night 🌈",
    "Good evening, Mili! Stay awesome ✨",
    "Hi Mili, enjoy your evening! 🌟",
    "Hello, Mili! Sweet dreams ahead 💖"
]

# List of random messages
random_messages = [
    "You are amazing 💛",
    "You make my world brighter 🌟",
    "You are my sunshine ☀️",
    "You inspire me every day 💖",
    "You are the best thing in my life 🌈",
    "You are loved more than words can say ✨",
    "You are my everything 💕",
    "You make life beautiful 🌸",
    "You are my greatest treasure 💎",
    "You are my heart and soul ❤️",
    "You are my reason to smile 😊",
    "You are the light in my life 🌟",
    "You make every moment special 💖",
    "You are my dream come true 🌈",
    "You are my forever love 💕",
    "You are the joy in my heart 🌸",
    "You are my greatest blessing 💎",
    "You are my perfect partner ❤️",
    "You are my happiness 💛",
    "You are my guiding star 🌟",
    "You are my safe haven 💖",
    "You are my everything 🌈",
    "You are my soulmate 💕",
    "You are my endless love 🌸",
    "You are my sunshine on a cloudy day 💎",
    "You are my heart's desire ❤️",
    "You are my best friend 💛",
    "You are my love story 🌟",
    "You are my treasure 💖",
    "You are my world 🌈",
    "You are my eternal flame 💕"
]

# Homepage route
@app.route('/')
def home():
    current_hour = datetime.now().hour
    if current_hour < 12:
        greetings = morning_greetings
    elif current_hour < 18:
        greetings = afternoon_greetings
    else:
        greetings = night_greetings

    random_greeting = greetings[datetime.now().day % len(greetings)]
    random_message = random_messages[datetime.now().day % len(random_messages)]

    # Select a random photo from the static/images folder
    image_folder = 'static/images/'
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    random_photo = random.choice(image_files)

    return render_template('home.html', greeting=random_greeting, random_message=random_message, random_photo=random_photo)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'your_password_here':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Incorrect password")
    return render_template('login.html')

# Mood Tracker route
@app.route('/mood', methods=['GET', 'POST'])
def mood():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    mood_data = []
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            mood_data = json.load(f)

    if request.method == 'POST':
        mood = request.form.get('mood')
        note = request.form.get('note')
        mood_entry = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "mood": mood,
            "note": note
        }
        mood_data.append(mood_entry)
        with open('data.json', 'w') as f:
            json.dump(mood_data, f)

    return render_template('mood.html', mood_data=mood_data)

@app.route('/delete_mood', methods=['POST'])
def delete_mood():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    date_to_delete = request.form.get('date')
    mood_to_delete = request.form.get('mood')

    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            mood_data = json.load(f)

        mood_data = [mood for mood in mood_data if not (mood['date'] == date_to_delete and mood['mood'] == mood_to_delete)]

        with open('data.json', 'w') as f:
            json.dump(mood_data, f)

    return redirect(url_for('mood'))

@app.route('/edit_mood', methods=['GET', 'POST'])
def edit_mood():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        date_to_edit = request.form.get('date')
        new_mood = request.form.get('new_mood')
        new_note = request.form.get('note')

        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                mood_data = json.load(f)

            for mood in mood_data:
                if mood['date'] == date_to_edit:
                    mood['mood'] = new_mood
                    mood['note'] = new_note

            with open('data.json', 'w') as f:
                json.dump(mood_data, f)

        return redirect(url_for('mood'))

    date_to_edit = request.args.get('date')
    mood_to_edit = request.args.get('mood')
    note_to_edit = request.args.get('note')

    return render_template('edit_mood.html', date=date_to_edit, mood=mood_to_edit, note=note_to_edit)

# Diary route
@app.route('/diary', methods=['GET', 'POST'])
def diary():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    diary_entries = []
    if os.path.exists('diary.json'):
        with open('diary.json', 'r') as f:
            diary_entries = json.load(f)

    if request.method == 'POST':
        entry = request.form.get('entry')
        diary_entry = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "entry": entry
        }
        diary_entries.append(diary_entry)
        with open('diary.json', 'w') as f:
            json.dump(diary_entries, f)

    return render_template('diary.html', diary_entries=diary_entries)

# Route to delete a diary entry
@app.route('/delete_diary', methods=['POST'])
def delete_diary():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    date_to_delete = request.form.get('date')
    entry_to_delete = request.form.get('entry')

    if os.path.exists('diary.json'):
        with open('diary.json', 'r') as f:
            diary_entries = json.load(f)

        diary_entries = [entry for entry in diary_entries if not (entry['date'] == date_to_delete and entry['entry'] == entry_to_delete)]

        with open('diary.json', 'w') as f:
            json.dump(diary_entries, f)

    return redirect(url_for('diary'))

# Route to edit a diary entry
@app.route('/edit_diary', methods=['GET', 'POST'])
def edit_diary():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        date_to_edit = request.form.get('date')
        new_entry = request.form.get('new_entry')

        if os.path.exists('diary.json'):
            with open('diary.json', 'r') as f:
                diary_entries = json.load(f)

            for entry in diary_entries:
                if entry['date'] == date_to_edit:
                    entry['entry'] = new_entry

            with open('diary.json', 'w') as f:
                json.dump(diary_entries, f)

        return redirect(url_for('diary'))

    date_to_edit = request.args.get('date')
    entry_to_edit = request.args.get('entry')

    return render_template('edit_diary.html', date=date_to_edit, entry=entry_to_edit)

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
