from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/read", methods=["GET"])
def read():
    file_name = request.args.get("file_name", "data/nofile.txt")
    with open(file_name, 'r') as f:
        file_content = f.read()
    return file_content

def count_words()

if __name__ == "__main__":
    app.run(debug=True)

#sudo docker build -t flaskapi:latest .
#sudo docker run -p 5000:5000 flaskapi:latest

#sudo docker-compose build
#sudo docker-compose up