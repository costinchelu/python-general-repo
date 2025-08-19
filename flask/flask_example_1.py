from flask import Flask, render_template

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
    return render_template("example_1.html")


# flask --app flask_example_1.py run
# or using the __name__:
if __name__ == "__main__":
    app.run(debug=True)