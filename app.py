from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def feed():
    test_posts= [
    "I can't wait to go to the park today",
    "I could really use a treat right now",
    "Aren't naps the best?"
    ]
    return render_template('index.html', posts=test_posts)
