Integrated Terminal VS Code
1. From the Command Palette (⇧⌘P), use the View: Toggle Integrated Terminal command.
2. To select a specific environment, use the Python: Select Interpreter command from the Command Palette (⇧⌘P).

3. python3 -m venv venv
4. source venv/bin/activate

5. pip install fastapi[all]
6. pip install --upgrade pip
7. uvicorn main:app --reload
8. http://127.0.0.1:8000/
9. http://127.0.0.1:8000/docs