"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

    wants_game = request.args.get("yesno")

    if wants_game:
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/game')
def game():
    """Greet user with compliment."""

    game_response = request.args.get("yesno")

    return render_template("game.html")

@app.route('/madlib')
def madlib():
    """Greet user with compliment."""

    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    name = request.args.get("name")

    return render_template("madlibs.html",
                            name=person,
                            noun=noun,
                            adjective=adjective,
                            color=color)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)