from flask import Flask, render_template, request, redirect
from PIL import Image, ImageDraw
import json
import requests



app = Flask(__name__, template_folder='Templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/<i>')
def anything(i):
    return redirect('/')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/physics')
def physics():
    return render_template('physics.html')

if __name__ == '__main__':
    app.run()