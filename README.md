# Personal Web App Gift for Mili

## Project Overview
This is a private and personal web app created as a birthday gift for Mili. The app is designed to be beautiful, cozy, and useful in her daily life.

### Features
1. **Homepage**
   - Displays a random photo and a personal greeting message.
   - Welcomes Mili by name.
   - Navigation buttons to other pages.

2. **Login Page**
   - Simple password login screen.
   - Redirects to the homepage after login.

3. **Mood Tracker Page**
   - Allows Mili to select her current mood and optionally add a note.
   - Saves mood entries to a local JSON file.
   - Displays mood trends over time.

4. **Diary Page**
   - Text area for writing daily diary entries.
   - Displays past entries.
   - Saves entries to a local JSON file.

### Technical Details
- **Backend**: Flask
- **Frontend**: Jinja2 templates
- **Data Storage**: JSON files
- **Styling**: Custom CSS

### Folder Structure
```
/my-wife-app
  /static
    /images          # Store photos for homepage
    /css             # Custom stylesheets
  /templates
    home.html
    login.html
    mood.html
    diary.html
  app.py
  requirements.txt
  README.md
```

### How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. Open the app in your browser at `http://127.0.0.1:5000`.

### Future Enhancements
- Add music playlists.
- Add a goals or wishlist page.
- Add daily self-care suggestions.
- Integrate messaging features.
