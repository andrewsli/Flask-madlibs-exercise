from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def show_form():
    return render_template("form.html", inputs=stories.story.prompts)


@app.route("/story")
def show_story():

    text = stories.story.generate(request.args)
    print(text)

    return render_template("story.html", story_text=text)
