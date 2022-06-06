from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
    
 
class PersonModel(db.Model):
    __tablename__ = "person"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    age = db.Column(db.Integer())

 
    def __init__(self, first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


 
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"

class Todo(db.Model):
    __tablename__ = "todo"

    id_of_task = db.Column(db.Integer() , primary_key = True)
    id_of_person = db.Column(db.Integer() , db.ForeignKey('person.id') , nullable = False)
    name_of_task = db.Column(db.String())

    def __init__(self, id_of_person, name_of_task):
        self.id_of_person = id_of_person
        self.name_of_task = name_of_task


