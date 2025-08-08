# Django to EXE Template

This project builds your Django app into a standalone `start.exe` file using GitHub Actions.

## 📦 How to Use

1. Replace the following with your files:
   - `mystorage/` → your Django project folder
   - `parts/` → your app folder
   - `db.sqlite3` → your database (optional)
   - `manage.py` → from your project
   - `requirements.txt` → from `pip freeze`

2. Push this to a GitHub repo.

3. GitHub Actions will build `start.exe` for you.

4. Download the `start.exe` from the Actions tab → Artifacts.

5. Run `start.exe` on any Windows machine, then go to `http://127.0.0.1:8000/` in a browser.

No Python or Django installation needed on that machine.