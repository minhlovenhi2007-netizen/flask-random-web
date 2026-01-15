from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mon_an = None

    if request.method == "POST":
        danh_sach_mon = [
            "bánh mì", "xôi", "mỳ cay", "mỳ trộn",
            "cơm thố", "bún riêu", "gà rán",
            "kimbap", "bún chả", "cơm gà"
        ]
        mon_an = random.choice(danh_sach_mon)

    return render_template("index.html", mon_an=mon_an)

@app.route("/random")
def random_page():
    return "Hello random"

if __name__ == "__main__":
    app.run()
