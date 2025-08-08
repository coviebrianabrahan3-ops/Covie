@echo off
cd /d %~dp0

REM Activate the virtual environment
call env\Scripts\activate

REM Run the Django server on 127.0.0.1 (localhost)
start http://127.0.0.1:8000
python manage.py runserver 127.0.0.1:8000

pause
