# import Flask class from flask module
from flask import Flask

# create flask app and save it to variable
app = Flask(__name__)

# define url of the app page and define a function which returns a content of a page
@app.route('/')
def home():
    return '<h1>Hello Flask!<h1>'

# use this part only when you run flask app with command `python app.py`. Enable debugging detect changes of app.py in the browser without the need to restart flask server
"""
if __name__ == "__main__":
    app.run(debug=True)
"""
