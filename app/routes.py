from app import myapp_obj, db
from flask import render_template, redirect, url_for, request, flash
from app.forms import RecipeForm, LoginForm
from app.models import Recipe, User
from flask_login import login_user, logout_user, current_user, login_required

@myapp_obj.route('/')
@myapp_obj.route('/recipes')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@myapp_obj.route('/recipe/<int:recipe_id>')
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@myapp_obj.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        print("FORM SUBMITTED BY:", current_user.username)
        new_recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            user=current_user
        )
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('recipe_form.html', form=form, title="Add Recipe")

@myapp_obj.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        flash("You can only delete your own recipes.")
        return redirect(url_for('index'))
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('index'))

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
