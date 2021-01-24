from flask import Flask, jsonify, request
from random import randrange

app = Flask(__name__)

MOVIES = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"]
    }
]


@app.route('/')
def start():
    return {'message': 'This endpoint is empty.'}


@app.route('/movies')
def movies():
    return jsonify(MOVIES), 200


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()

    MOVIES.append(movie)

    return jsonify({'id': randrange(len(MOVIES), len(MOVIES)*100)}), 201


@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    MOVIES[index] = movie
    return jsonify(MOVIES[index]), 200


@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    MOVIES.pop(index)
    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
