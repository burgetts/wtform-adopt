from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app) 

@app.route('/')
def show_all_pet_listing():
    """Homepage that shows all pet listings."""

    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=["GET","POST"])
def add_pet():
    """Form to add new pet."""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:

        return render_template('add_pet.html', form=form)

@app.route('/<pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Detail page containing pet editing form."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditForm()
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        pet.photo_url = photo_url
        pet.notes = notes
        pet.avilable = available
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/{pet.id}')
    return render_template('pet_detail.html', pet=pet, form=form)
