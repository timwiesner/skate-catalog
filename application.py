from flask import Flask, render_template, request, redirect, jsonify, url_for
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
@app.route('/catalog/new', methods = ['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newCategory.html')



# Show category route
@app.route('/catalog/<int:category_id>')
def showCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    # items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('category.html', category=category)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
