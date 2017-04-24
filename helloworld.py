"""
Basic Hello, World webpage.

Defaults to running on port 5000

In the activated virtualenv:
python helloworld.py
"""
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    """."""
    return "Hello, World!"

# start the development server using the run() method
# '0.0.0.0' allows external access
if __name__ == "__main__":
    app.run('0.0.0.0')
