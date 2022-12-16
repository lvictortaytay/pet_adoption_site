from flask import Flask,request
from random import choice
from flask.templating import render_template
from app import Story

app=Flask(__name__)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved {plural_noun}."""
)

class Story2:
    def __init__(self,code_name,title,words,text):
        self.code_name = code_name
        self.title = title
        self.words = words
        self.sentence = text

    def generate(self,sub_words):
        sentence = self.sentence
        for (key, val) in sub_words.items():
            #redifining the sentence or modifying it
            sentence = sentence.replace("{" + key + "}", val) #replace the key for the value for the sentence

        return sentence #returning the new sentence



story1 = Story2(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story2(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)
story3 = Story2(
    "dogs",
    "a phlight to paws",
    ["plural_noun", "verb"],
    """dogs!! they love to {verb} {plural_noun}!"""
)
story4 = Story2(
    "airplanes",
    "a sky high soar story",
    ["noun", "verb","adjective"],
    """while {noun} was flying the {adjective} plane he saw a {noun} !"""
)
story5 = Story2(
    "highschool",
    "a day in the life of a teen",
    ["noun", "verb", "adjective" , "plural_noun"],
    """while walking through the halls , i saw a {noun} making a b line for {noun} while {verb} thier {adjective} hair"""
)


stories = {s.code_name: s for s in [story1, story2,story3,story4,story5]} #this makes a dictionary with the keys as the keys for the given stories to select from


@app.route("/")
def selection():
    selections = stories
    return render_template("selection.html",story=selections)


story_id_holder = ""

@app.route("/new-form")
def new_form():
    selections = stories
    story_id = request.args["story_id"]
    story_id_holder = story_id
    print(story_id_holder)
    story = stories[story_id]
    words = story.words
    return render_template("new-form.html",story=words,story_id=story_id)



@app.route("/new-story")
def new_story():
    values = request.args
    story_id = request.args["story_id"]
    story = stories[story_id]
    text = story.generate(values)
    return render_template("new-story.html",new_story=text)










Prompts = story.prompts
print(Prompts)
@app.route("/home")
def test():
    Prompts = story.prompts
    return render_template("base.html",Prompts=Prompts)



@app.route("/story")
def story_page():
    new_story = story.generate(request.args)
    return render_template("story.html",new_story=new_story)