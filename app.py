from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Cloud Technologies Laboratory</h1><p>Welcome to our cloud web application!</p>"

@app.route("/about")
def about():
    return "<h2>About</h2><p>Laboratory work on Cloud Technologies and CI/CD.</p>"

@app.route("/contact")
def contact():
    return "<h2>Contact</h2><p>Student: Askarov Sultanal | Phone: 8(777)123-45-67</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)