from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_router():
    return {"R1": "192.168.0.10"}

if __name__ == "__main__":
    app.run()