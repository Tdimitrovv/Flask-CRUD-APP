from flask import Flask,render_template,request,redirect
from models import db,PersonModel,Todo
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']

        person = PersonModel(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        db.session.add(person)
        db.session.commit()
        return redirect('/')

@app.route('/create_task' , methods = ['GET','POST'])
def create_task():
    if request.method == 'GET':
        return render_template('createpage_task.html')
 
    if request.method == 'POST':

        name_of_task = request.form['name_of_task']
        Id_of_person = request.form['id_of_person']


        Todo_task = Todo(
            id_of_person=Id_of_person,
            name_of_task=name_of_task
        )
        db.session.add(Todo_task)
        db.session.commit()
        return redirect('/tasks')

 
 
@app.route('/')
def RetrieveList():
    person = PersonModel.query.all()
    return render_template('datalist.html',person = person)



@app.route('/<int:id_of_person>/tasks')
def RetrieveList_tasks(id_of_person):
    todo = Todo.query.filter_by(id_of_person = id_of_person)
    if todo:
        return render_template('datalist_tasks.html',todo = todo)
    return f"No tasks are assigned to id = {id_of_person}"

@app.route('/tasks')
def RetrieveList_all_tasks():
    ToDo = Todo.query.all()
    return render_template('datalist_tasks.html',todo = ToDo)
    
 
 
 
@app.route('/<int:id>')
def RetrievePerson(id):
    person = PersonModel.query.filter_by(id=id).first()
    if person:
        return render_template('data.html', person = person)
    return f"Employee with id ={id} Doesnt exist"
 
 
@app.route('/<int:id>/edit',methods = ['GET','POST'])
def update(id):
    person = PersonModel.query.filter_by(id=id).first()


    if request.method == 'POST':
        if person:
            db.session.delete(person)
            db.session.commit()


        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']


        person = PersonModel(
            first_name=first_name,
            last_name=last_name,
            age=age,

        )
        db.session.add(person)
        db.session.commit()
        return redirect('/')
        return f"Student with id = {id} Does not exist"
 
    return render_template('update.html', person = person)


@app.route('/<int:id_of_task>/edit_task',methods = ['GET','POST'])
def update_task(id_of_task):
    todo = Todo.query.filter_by(id_of_task=id_of_task).first()


    if request.method == 'POST':
        if todo:
            db.session.delete(todo)
            db.session.commit()


        id_of_person = request.form['id_of_person']
        name_of_task = request.form['name_of_task']
        

        todo = Todo(
            id_of_person=id_of_person,
            name_of_task=name_of_task,
            

        )
        db.session.add(todo)
        db.session.commit()
        return redirect('/tasks')
        return f"Student with id = {id} Does not exist"
 
    return render_template('update_task.html', todo = todo)
 
 
 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    person = PersonModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if person:
            db.session.delete(person)
            db.session.commit()
            return redirect('/')
        abort(404)
   
    return render_template('delete.html')
 


@app.route('/<int:id_of_task>/delete_task', methods=['GET','POST'])
def delete_task(id_of_task):
    todo = Todo.query.filter_by(id_of_task=id_of_task).first()
    if request.method == 'POST':
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return redirect('/tasks')
        abort(404)
   
    return render_template('delete_task.html')
 
app.run(host='localhost', port=5000)