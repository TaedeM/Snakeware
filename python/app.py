import json
import math
from flask import Flask, jsonify, Response, render_template


def create_json(*args, **kwargs):
    # Function that creates json without alphabetically sorting the keys (jsonify from Flask does this)
    return Response(json.dumps(dict(*args, **kwargs), sort_keys=False), mimetype='application/json')


def is_prime(number):
    # From: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

    # Base case
    if number <= 1:
        return False

    # Check if number is prime
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            # Number is not prime
            return False

    # Number is prime
    return True


def is_fibonacci(number):
    # Function that checks if 'number' is one of the first 52 Fibonacci numbers
    # It generates each next number in the Fibonacci sequence untill:
    #   1 - The input number has been found as a Fibonacci number
    #   2 - The maximum iterations are exceeded
    #   3 - The input number is smaller than the next Fibonacci number
    # Adapted from: https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/

    # Base cases
    if number < 0:
        return False
    if number == 0:
        return True

    # Initialization
    max_iter = 51
    n1 = 0
    n2 = 1
    next_number = n2
    count = 1

    # Check if number is in Fibonacci sequence
    while count <= max_iter and number >= next_number:
        count += 1
        if number == next_number:
            return True

        n1, n2 = n2, next_number
        next_number = n1 + n2

    # Number is not in Fibonacci sequence
    return False


app = Flask(__name__)


# Default route, displays basic information
@app.route('/')
def landing_page():
    return render_template('index.html')


# Default route for the API, displays only '{}'
@app.route('/api/')
def nothing():
    return jsonify({})


# Route for calculating both prime and Fibonacci
# Using <string> instead of <int>, as int does not recognize negative values
@app.route('/api/<string:n>', methods=['GET'])
def prime_fib(n):
    try:
        n = int(n)
    except ValueError:
        return jsonify({'error': 'Please provide a valid integer'}), 400
    return create_json({'input_number': n,
                        'prime': is_prime(n),
                        'fibonacci': is_fibonacci(n)})


# Route for calculating prime
@app.route('/api/prime/<string:n>', methods=['GET'])
def prime(n):
    try:
        n = int(n)
    except ValueError:
        return jsonify({'error': 'Please provide a valid integer'}), 400
    return create_json({'input_number': n,
                        'prime': is_prime(n)})


# Route for calculating Fibonacci
@app.route('/api/fibonacci/<string:n>', methods=['GET'])
def fibonacci(n):
    try:
        n = int(n)
    except ValueError:
        return jsonify({'error': 'Please provide a valid integer'}), 400
    return create_json({'input_number': n,
                        'fibonacci': is_fibonacci(n)})


app.run()
