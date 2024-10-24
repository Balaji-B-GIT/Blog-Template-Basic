from flask import Flask, render_template, url_for
from post import Post

app = Flask(__name__)
post = Post()

data = post.get_data()

@app.route('/')
def home():
    return f"<h1>Click here to see <a href ={url_for("get_blogs")}>My Blogs</a></h1>"


@app.route('/blog')
def get_blogs():
    return render_template("index.html",blogs = data)

@app.route('/post/<int:blog_id>')
def blog(blog_id):
    if post.get_blog_by_id(blog_id):
        return render_template("post.html",blog = post.get_blog_by_id(blog_id))
    else:
        return "Blogs not found",404


if __name__ == "__main__":
    app.run(debug=True)
