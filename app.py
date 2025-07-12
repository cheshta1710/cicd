import flask 
myapp=flask.Flask(__name__)
@myapp.route("/info")
def newinfo():
    return "this cicd pipeline"
@myapp.route("/mail")
def newmail():
    return "this is second function for my cicd pipeline"
myapp.run(host="0.0.0.0", port=5000)
