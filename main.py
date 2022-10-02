from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    access = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=access)

@app.route('/post/<num>')
def get_post(num):
    access = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template('post.html', post=access[int(num)-1])

if __name__ == "__main__":
    app.run(debug=True)

