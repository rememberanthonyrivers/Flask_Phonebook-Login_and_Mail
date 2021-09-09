from flask import Flask 

@app.route("/") 
def hello_world():
    title = "HOME"
    fav_five = ['Drake', 'Kanye', 'Joe Biden', 'Lebron James', 'Micheal Jordan']
    return render_template('base.html', title=title, items=ItemsView)

@app.route("/register")
def register():
    title = 'Register'
    return render_template('register.html', title=title) 

@app.route('/home')
def home():
    title="Home"
    return '<h1>This is the Homepage.</h1>' 

@app.route('/register_phone_number')
def register_phone_number():
    title="Phone Database"
    return render_template('base.html', title=title, items=ItemsView)