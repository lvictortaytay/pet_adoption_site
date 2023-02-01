from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db , connect_db , Pet
from forms import addDoggy , editDoggy


app = Flask(__name__)


app.config["SECRET_KEY"] = "blahblah112233"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
connect_db(app)





@app.route("/")
def homepage():
    pets = Pet.query.all()
    return render_template("home.html" ,pets = pets)
    


@app.route("/add",methods=["POST" , "GET"])
def add_pup():
    form = addDoggy()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name = name , species = species , photo_url = photo_url , age = age , notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        print(name)
        return redirect("/")
    else:
        return render_template("addpup.html" , form = form)
    

@app.route("/info/<int:id>" , methods = ["GET" , "POST"])
def puppy_info(id):
    pet = Pet.query.get(id)
    form = editDoggy()
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        print(pet.available)
        return redirect("/")
    else:
        return render_template("info.html" , pet = pet , form = form)
