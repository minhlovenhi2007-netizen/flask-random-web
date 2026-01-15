from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    numbers = list(range(1, 101))
    random_number = random.choice(numbers)
    return render_template("index.html", number=random_number)

if __name__ == "__main__":
    app.run(debug=True)
