from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def feed():

    post1 = {
        "Text":"I can't wait to go to the park today",
        "Name":"Melba",
        "Username":"melba",
        "LikeCount":10,
        "CommentCount":4,
        "DateTime": datetime(2021,7,1,17,0,0),
        "Picture": "melba_profile.png"
    }
    post2 = {
        "Text":"I could really go for a treat right now",
        "Name":"Melba",
        "Username":"melba",
        "LikeCount":25,
        "CommentCount":15,
        "DateTime": datetime(2021,8,4,17,2,5),
        "Picture": "melba_profile.png"
    }
    test_posts= [post1,post2]
    return render_template('index.html', posts=test_posts)
