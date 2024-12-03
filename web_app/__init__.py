# this is the "web_app/__init__.py" file...

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.stocks_routes import stocks_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(stocks_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)