from crypt import methods
from flask import Blueprint, render_template, redirect, url_for, request

post_pages = Blueprint("posts", __name__)

@post_pages.get("/post/<string:title>")
def display_post(title: str):
    return "Display post page."

@post_pages.route("/post/", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        # TODO: We can create the post in our database here
        return redirect(url_for(".display_post", title=title))
    return render_template("new_post.html") 