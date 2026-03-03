from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Главная"

@app.route("/about")
def about():
    return "О нас"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Пост {post_id**2}"

if __name__ == "__main__":
    app.run(debug=True)