import os
import time
import webbrowser
import subprocess
import sys

def main():
    # Change to current directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Try to run Django server
    try:
        subprocess.Popen(["python", "manage.py", "runserver", "--noreload", "127.0.0.1:8000"])
    except Exception as e:
        print("Error running server:", e)
        sys.exit(1)

    # Wait a few seconds for the server to start
    time.sleep(3)

    # Open browser to local server
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    main()
