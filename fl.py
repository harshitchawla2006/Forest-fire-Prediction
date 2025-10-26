from flask import Flask,render_template,request
#This code creates an instance of the Flask class, which acts as the Web Server Gateway Interface (WSGI) application.
#The __name__ parameter is important and should not be skipped.
app = Flask(__name__)


#Define a route for the root URL ("/") using the @app.route decorator.
@app.route("/")
def welcome():
    return "<html> <h1>Welcome to Flask</h1> </html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello, {name}!"
    return render_template("form.html")

@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Form submitted! Hello, {name} Bhosdu!"
    return render_template("submit.html")
#To define the entry point of the application, use the following condition:
if __name__ == "__main__":
    app.run(debug=True)   
#Setting debug=True enables debug mode, which automatically restarts the server whenever code changes are made. This is useful during development.     