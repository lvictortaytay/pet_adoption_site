from io import StringIO
from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField , FloatField
from wtforms.validators import InputRequired , URL , Optional , NumberRange, AnyOf


class addDoggy(FlaskForm):
    name = StringField("puppy name" , validators=[InputRequired()])
    species = StringField("puppy species")
    photo_url = StringField("puppy picture url!" , validators=[URL()])
    age = FloatField("puppy age!" , validators=[NumberRange(min = 0 , max = 30 , message="enter a number between 0 and 30 ")] )
    notes = StringField("notes")



class editDoggy(FlaskForm):
    photo_url = StringField("puppy picture url!" , validators=[URL()])
    notes = StringField("notes")
    available = StringField("available")
