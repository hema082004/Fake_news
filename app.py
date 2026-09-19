from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Fake News Detection System</h1><p>Vercel Flask is working!</p>"
