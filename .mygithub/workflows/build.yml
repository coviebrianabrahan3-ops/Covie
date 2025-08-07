name: Build EXE

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pyinstaller
        pip install -r mystorage/requirements.txt

    - name: Build EXE
      run: pyinstaller mystorage/start.py --onefile --noconsole --name=mystorage_app

    - name: Upload EXE
      uses: actions/upload-artifact@v4
      with:
        name: mystorage_app
        path: dist/mystorage_app.exe
        
