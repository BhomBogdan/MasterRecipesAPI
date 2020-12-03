from flask import Flask


from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)

class Recipe(db.Model):



    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(80), nullable=False)
    time = db.Column(db.String(80), nullable=False)
    URL = db.Column(db.String(80), nullable=False)
    idn = db.Column(db.String(10), nullable=False)

    def json(self):
        return{'URL':self.URL, 'tittle':self.tittle, 'time':self.time, 'idn':self.idn}

    def add_recipes(_URL, _tittle, _time, _idn):
            new_recipe = Recipe(URL=_URL, tittle=_tittle, time=_time, idn=_idn)
            db.session.add(new_recipe)
            db.session.commit()

    def add_recipe_URL(_URL,_tittle,_time):
            new_recipe = Recipe(URL=_URL,tittle="Null", time=" ")
            db.session.add(new_recipe)
            db.session.commit()
            

    def get_all_recipes():
        return [Recipe.json(recipe) for recipe in Recipe.query.all()]

    def get_recipe(_idn):
        return Recipe.json(Recipe.query.filter_by(idn=_idn).first())

    def detelete_recipe(_id):
        Recipe.query.filter_by(id=_id).delete()
        db.session.commit()

    
    
    def __repr__(self):
        recipe_object = {
            'URL':self.URL,
            'idn':self.idn,
            'tittle':self.tittle,
            'time':self.time
        }
        return json.dumps(recipe_object)



