from typing import ItemsView
from flask import Flask
from flask import render_template 

app = Flask(__name__)

# @app.route("/") 
# def hello_world():
    # title = "HOME"
    # return render_template('base.html', title=title, items=ItemsView)

@app.route("/") 
def hello_world():
    title = "HOME"
    fav_five = ['Drake', 'Kanye', 'Joe Biden', 'Lebron James', 'Micheal Jordan']
    return render_template('base.html', title=title, items=ItemsView)

@app.route("/register")
def register():
    title = 'Register'
    return render_template('register.html', title=title) 


if __name__ == "__main__":
    app.run() 
