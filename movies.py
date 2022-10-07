from flask import Flask, jsonify, request
app = Flask(__name__)

movies = [
    {
        "name": "Squid Game",
        "casts": ["Lee Kwon Yu", "Lee Monsuk", "Young Sheewon"],
        "genres": ["Thriller", "Comedy"],
    },
    {
        "name": "Little Women",
        "casts": ["Rosemarie Chavez", "Heart Ebange", "Joana Miguel"],
        "genres": ["Drama", "Suspence"],
    },
]

@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify(movies)

@app.route("/movies", methods=["POST"])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {"id": len(movies)}, 200

@app.route("/movies/<int:index>", methods=["DELETE"])
def delete_movie(index):
    movies.pop(index)
    return "Movies was successfully deleted.", 200

if __name__ == "__main__":
    app.run()