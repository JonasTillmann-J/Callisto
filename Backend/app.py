from flask import Flask, render_template

app = Flask(__name__)

@app.router('/')
def index():
    return render_template('index.html')