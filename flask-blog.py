from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Szymon Ruszała",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 20, 2021",
    },
    {
        "author": "Szymon Ruszała",
        "title": "Blog post 2",
        "content": "First post content",
        "date_posted": "April 20, 2021",
    },
    {
        "author": "Szymon Ruszała",
        "title": "Blog post 3",
        "content": "First post content",
        "date_posted": "April 20, 2021",
    },
]


@app.route("/")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
