import flask
from car_detection import detectAndCountCars


app = flask.Flask(__name__)

@app.route('/') # on load of page
def hello():
    return "Hello, World!"



if __name__ == '__main__':
    app.run()