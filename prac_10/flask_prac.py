"""
CP1404 Flask Practical
"""

from flask import Flask

app = Flask(__name__)


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


@app.route('/')
def home():
    """Home page with big heading."""
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Michael Rozis"):
    return f"Hello {name}"


@app.route('/c_to_f/<celsius_str>')
def c_to_f(celsius_str):
    """Convert Celsius from URL to Fahrenheit."""
    try:
        celsius = float(celsius_str)
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        return f"<p>{celsius} °C is {fahrenheit:.2f} °F</p>"
    except ValueError:
        return "<p>Invalid temperature - please use a number.</p>"


if __name__ == '__main__':
    app.run(debug=True)