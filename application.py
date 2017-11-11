from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///skatecatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Home page route
@app.route('/')
@app.route('/catalog')
def hello():
    return render_template('catalog.html')

# # Show category route
# @app.route('/catalog/<str:category_id>')
# def showCategory(category_id):
#     category = session.query(Category).filter_by(name=category_id).one()
#     items = session.query(Item).filter_by(category_id=category_id).all()



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
