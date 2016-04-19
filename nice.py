from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "Hi! This is the home page. <br>To get to a better page click <a href='/hello'>HERE</a>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

        <form action="/greet">
          <label>Select Your "Compliment": </label>
          <select name="compliment">
            <option value="nice sometimes">Nice</option>
            <option value="pretty from some angles">Pretty</option>
            <option value="smart for a toddler">Smart</option>
          </select>
          <label>What's your name? <input type="text" name="nice-person"></label>
          <input type="submit">
        </form>

        <form action="/diss">
          <label>Select Your "Diss": </label>
          <select name="diss">
            <option value="a real jerk">Nice</option>
            <option value="fooling yourself">Pretty</option>
            <option value="dumber than a box of hair">Smart</option>
          </select>

          <label>What's your name? <input type="text" name="diss-person"></label>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    
    player1 = request.args.get("nice-person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player1, compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""
    
    player2 = request.args.get("diss-person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Rude Awakening</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player2, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
