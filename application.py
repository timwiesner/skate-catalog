from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///skatecatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Home / Show All Categories
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).all()
    return render_template('catalog.html', categories=categories)


# Create a new category
@app.route('/catalog/new/', methods = ['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        flash('New category created!')
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newCategory.html')


# Edit category
@app.route('/catalog/<int:category_id>/edit/', methods = ['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category edited!')
            return redirect(url_for('showCatalog'))
    else:
        return render_template('editCategory.html', category=editedCategory)


@app.route('/catalog/<int:category_id>/delete/', methods = ['GET', 'POST'])
def deleteCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(deletedCategory)
        session.commit()
        flash('Category deleted!')
        return redirect(url_for('showCatalog'))
    else:
        return render_template('deleteCategory.html', category=deletedCategory)


# Show specific category route
@app.route('/catalog/<int:category_id>/')
def showCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('category.html', category=category)


# Add item
@app.route('/catalog/<int:category_id>/new/', methods = ['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = Item(name=request.form['name'])
        session.add(newItem)
        session.commit()
        flash('New item created!')
        return redirect(url_for('showCategory', category_id=category_id))
    else:
        return render_template('newItem.html')



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
