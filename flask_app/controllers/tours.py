from flask import render_template,redirect,request,session,flash
from flask_app import app, bcrypt
from flask_app.models.tour import Tour
from flask_app.models.user import User


# @app.route('/')
# @app.route('/sightings')
# def all_recipes():
#     sightings = Sightings.get_all()
#     print(sightings)
#     return render_template('index.html', all_sightings = sightings)


@app.route('/new')
def new_tour():

    context = {
        'user' : User.get_one({'id':session['user_id']})
    }

    return render_template('new.html', **context)



@app.route('/create_tour', methods=['POST'])
def create_tour():


    is_valid = Tour.validate_tour(request.form)

    if not is_valid:
        return redirect('/new')

    data = {
        **request.form,
        'user_id' : session['user_id']
        # "name": request.form["name"],
        # "description": request.form["description"],
        # "instructions" : request.form["instructions"],
        # "date_made_on" : request.form["date_made_on"],
    }
    # Call the save @classmethod on User
    Tour.create(data)
    # store user id into session

    return redirect("/dashboard")

@app.route('/tour/<int:id>/show')
def show_tour(id):
    context = {
        'user': User.get_one({'id': session['user_id']}),
        'tour': Tour.get_one({'id': id})

    }
    return render_template("tour.html", **context)


@app.route('/edit/<int:id>')
def edit_tour(id):

    tour = Tour.get_one({'id': id})

    if tour.user_id != session['user_id']:
        return redirect('/')

    context = {
        'user': User.get_one({'id': session['user_id']}),
        'tour' : tour
    }
    return render_template('edit.html', **context)



@app.route('/tour/<int:id>/update', methods=["POST"])
def update_tour(id):

    tour = Tour.get_one({'id': id})

    if tour.user_id != session['user_id']:
        return redirect('/')

    is_valid = Tour.validate_tour(request.form)

    if not is_valid:
        return redirect(f'/edit/{id}')

    data = {
        **request.form,
        'id':id
        # 'recipe' : recipe
    }
    tour = Tour.update(data)
    return redirect('/dashboard')


@app.route('/tour/<int:id>/delete', methods=['POST'])
def delete_Tour(id):

    tour = Tour.get_one({'id': id})

    if tour.user_id != session['user_id']:
        return redirect('/')

    Tour.delete_tour({'id': id})
    return redirect('/dashboard')