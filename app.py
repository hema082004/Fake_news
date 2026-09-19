from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fake News Detection</title>
    </head>
    <body>
        <h1>Fake News Detection System</h1>
        <p>Vercel Flask is working successfully!</p>
    </body>
    </html>
    """
