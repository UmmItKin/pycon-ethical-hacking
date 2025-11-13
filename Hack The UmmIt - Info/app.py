import os
from flask import Flask, request, session, redirect, send_from_directory
from dotenv import load_dotenv
import subprocess

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_insecure_key")

USERNAME = os.getenv("ADMIN_USERNAME", "admin")
PASSWORD = os.getenv("ADMIN_PASSWORD", "398104521h")
FLAG_PATH = os.getenv("FLAG_PATH", "flag.txt")

UPLOAD_FOLDER = "./uploads"
PORT = int(os.getenv("FLASK_PORT", 8080))

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username") == USERNAME and request.form.get("password") == PASSWORD:
            session["logged_in"] = True
            return redirect("/admin")
        else:
            return "<h3>Invalid credentials</h3>"
    return '''
        <h2>Login Page</h2>
        <form method="POST">
          Username: <input name="username"><br>
          Password: <input type="password" name="password"><br>
          <input type="submit" value="Login">
        </form>
        <h1>玩爛了再叫我 reboot 整台機器就好了 XD</h1>
        <h1>By: UmmIt Kin</h1>
    '''

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get("logged_in"):
        return redirect("/")
    if request.method == "POST":
        uploaded = request.files.get("file")
        if uploaded:
            filepath = os.path.join(UPLOAD_FOLDER, uploaded.filename)
            uploaded.save(filepath)
            return f"<p>File uploaded to: {filepath}</p>"
    return '''
        <h2>Admin Panel</h2>
        <form method="POST" enctype="multipart/form-data">
          <input type="file" name="file"><br>
          <input type="submit" value="Upload File">
        </form>
        <br>
        <a href="/lfi?file=app.py">Test LFI reading app.py</a>
        <br>
        <a href="/exec?cmd=ls">Test Command Injection</a>
    '''

@app.route("/uploads/<path:filename>")
def uploaded(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/lfi")
def lfi():
    target_file = request.args.get("file")
    if not target_file:
        return "<h3>Usage: /lfi?file=PATH</h3>"
    try:
        with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
            return f"<pre>{f.read()}</pre>"
    except Exception as e:
        return f"<p>Error: {e}</p>"

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")
    if not cmd:
        return "<h3>Usage: /exec?cmd=COMMAND</h3>"
    try:
        output = subprocess.getoutput(cmd)
        return f"<pre>{output}</pre>"
    except Exception as e:
        return f"<p>Error: {e}</p>"

@app.route("/flag")
def show_flag():
    try:
        with open(FLAG_PATH, "r") as f:
            return f"<pre>{f.read()}</pre>"
    except Exception as e:
        return f"<p>Error: {e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
