from flask import Flask, render_template, abort
from data import test_posts, dogs
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'melba': generate_password_hash("melba")
}

@auth.verify_password #Has to do with the library
def verify_password(username, password): #Designed to work with encrypted passwords
    if username in users and \
            check_password_hash(users.get(username), password):
        return username #Checks if password is valid

@app.route("/")
@auth.login_required
def feed():
    return render_template('feed.html', user = auth.current_user(), posts=test_posts, title = "My Feed")

@app.route("/comments/<int:post_id>")
def comments(post_id):
    post=test_posts[post_id]
    return render_template('comments.html',title = "Comments", post=post)

@app.route("/dog/<string:username>")
@auth.login_required
def profile(username):
    dog = dogs[username]
    return render_template('profile.html', title = dog['Name'], dog = dog)

@app.route("/logout")
def logout():
    return abort(401)

if __name__ == "__main__":
    app.run(debug = True)
