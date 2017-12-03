from flask import render_template, jsonify
from flask.ext.login import current_user, login_required
from app import app
import random


@app.route('/')
def index():
    return render_template('index.html', title='Home', current_user=current_user)

@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(14.5504938, 14.6004938),
               random.uniform(120.9896386,  120.9996386))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})

@app.route('/qoute')
def qoute():
    return render_template('pages/qoute.html', title='Quotation')

@app.route('/search-results')
def searh_results():
    return render_template('pages/search-results.html', title='Search Results')

@app.route('/search')
def search():
    return render_template('pages/search.html', title='Search')

@app.route('/profile/reviews')
def profile_reviews():
    return render_template('pages/profile/reviews.html', title='Reviews')

@app.route('/profile/services')
def profile_services():
    return render_template('pages/profile/services.html', title='Services')

@app.route('/looking-for')
def lookingfor():
    return render_template('pages/looking-for.html', title='Service')