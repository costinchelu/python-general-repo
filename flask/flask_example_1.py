from flask import Flask

app = Flask(__name__)

# flask --app flask_example_1.py run
# or using the __name__:
if __name__ == "__main__":
    app.run()


# decorator from Flask Framework:
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


