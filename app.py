from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "something"
debug = DebugToolbarExtension(app)


@app.route('/')
def questions_func():
  """Generate form for inputs that will be used for the story"""

  placeholders = story.placeholders
  return render_template("questions.html", placeholders=placeholders)


# new_dict = {"place": "Mars", "noun":"dog", "adjective":"happy", "verb":run, "plural_noun": "squirrels" }

@app.route('/story')
def show_story():
  """Show story"""
  # request.args is a dictionary where the string queries are stored; can test with new_dict 
  text = story.generate(request.args)
  return render_template("story.html", text=text)