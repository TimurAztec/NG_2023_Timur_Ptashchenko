from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

files = [f for f in os.listdir("./static/images") if os.path.isfile(os.path.join("./static/images", f))]

@app.route('/')
def index():
    img = random.choice(files)
    return redirect(f'/img/{img}')

@app.route('/img/<string:img_name>')
def img(img_name):
    index = files.index(img_name)

    prev_index = (index - 1) % len(files)
    next_index = (index + 1) % len(files)

    prev = files[prev_index]
    next = files[next_index]
    return render_template("index.html", img=url_for('static', filename=f'images/{img_name}'), prev=prev, next=next)

app.run(port=8080)