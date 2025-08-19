from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


# (route) decorator from Flask Framework:
@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """https://flask.palletsprojects.com/en/stable/quickstart/#routing"""
    return f'Post {post_id}'


@app.route("/render")
def render_html():
    random_number = random.randint(1, 10)
    return render_template("example_1.html", num=random_number)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    age_url = f"https://api.agify.io?name={name}"
    gender_data = requests.get(gender_url).json()
    age_data = requests.get(age_url).json()
    gender = gender_data["gender"]
    age = age_data["age"]
    animals = ["cow", "chicken"]
    return render_template("example_1.html", name=name, gender=gender, age=age, animals=animals)


@app.route("/blog")
def get_blog():
    return render_template("blog.html")


# flask --app flask_example_1.py run
# or using the __name__:
if __name__ == "__main__":
    app.run(debug=True)