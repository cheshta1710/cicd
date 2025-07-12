import flask 

myapp=flask.Flask(__name__)

@myapp.route("/")
def home():
    return "Welcome to home page."
@myapp.route("/login")
def login():
    return "This is the login page."
@myapp.route("/aboutus")
def about():
    return "This is about us page."
@myapp.route("/mail")
def mail():
    return "This is the mail page."
@myapp.route("/contact")
def contact():
    return "This is the contact us page."
@myapp.route("/links")
def links():
    return "This is the links page where you will find all social media links."
myapp.run(host="0.0.0.0", port=5000)
