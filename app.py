from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        names = ["An", "Bình", "Cường", "Dũng", "Hà"]
        result = random.choice(names)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
