from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

#provided story instance contains a prompts (list) and a text attribute (string)
#and a generate method that creates a custom story based on a passed in dictionary
#the keys in the dictionary must correspond to the prompts

STORY_OPTIONS = {
    "default": stories.story,
    "the-gym": stories.the_gym
}


@app.route("/madlib/")
def show_form():
    """
    landing page creates a form based on story_instance.prompts

    form sends user to /story
    """
    curr_story = request.args["story-object"]

    story_prompts = STORY_OPTIONS[curr_story].prompts

    return render_template("madlib_form.html", inputs=story_prompts, story_id=curr_story)


# @app.route("/story")
# def show_story():
#     """
#     makes new madlibs text based on the request.args dictionary (immutable multi dict)
#     """
#     # text = curr_story.generate(request.args)

#     # return render_template("story.html", story_text=text)
