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
        <p>Vercel deployment is working successfully!</p>
    </body>
    </html>
    """

@app.route("/api/test")
def test():
    return {
        "status": "success",
        "message": "Fake News API is working"
    }
