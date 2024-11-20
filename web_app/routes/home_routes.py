# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")

    # if the request contains url params,
    # for example a request to "/hello?name=Harper"
    # the request.args property will hold the values in a dictionary-like structure
    # can be empty like {} or full of params like {"name":"Harper"}
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)

    # access "name" key if present, otherwise use default value
    name = url_params.get("name") or "World"

    message = f"Hello, {name}!"

    x = 5
    #return message
    return render_template("hello.html", message=message, x=x, y=20)