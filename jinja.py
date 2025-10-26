from flask import Flask,render_template,request,redirect,url_for
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
        name=request.form.get('name', '')
        if name:
            return f"Form submitted! Hello, {name}!"
        else:
            return render_template("form.html", error="Please enter a name")
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    res=""
    if(score>=50):
        res="You are passed"
    else:
        res="You are failed"
    return render_template("success.html",result=res)     # resuls is variable which is passed to success.html file

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if(score>=50):
        res="You are passed"
    else:
        res="You are failed"
    exp={ "score":score, "result":res}    
    return render_template("success.html",results=exp)     # resuls is variable which is passed to success.html file 

@app.route("/getresult",methods=["GET","POST"])
def getresult():
    if request.method=='POST':
        try:
            # Get form data with error handling
            data_science = float(request.form.get('data_science', 0))
            c = float(request.form.get('c', 0))
            
            # Validate scores are within reasonable range
            if data_science < 0 or data_science > 100 or c < 0 or c > 100:
                return render_template("error.html", 
                                     message="Scores must be between 0 and 100")
            
            # Calculate total score
            total_score = (data_science + c) / 2
            
            # Redirect to success page with the calculated score
            return redirect(url_for('successres', score=int(total_score)))
            
        except (ValueError, TypeError) as e:
            return render_template("error.html", 
                                 message="Please enter valid numeric scores")
        except Exception as e:
            return render_template("error.html", 
                                 message="An error occurred while processing your request")
    
    # Handle GET request - show form or redirect
    return render_template("score_form.html")    



#To define the entry point of the application, use the following condition:
if __name__ == "__main__":
    app.run(debug=True)   
#Setting debug=True enables debug mode, which automatically restarts the server whenever code changes are made. This is useful during development.     