from flask import render_template, jsonify
from app import app
import random


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(14.5504938, 14.6004938),
               random.uniform(120.9896386,  120.9996386))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
