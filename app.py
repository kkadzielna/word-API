from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)

#sudo docker build -t flaskapi:latest .
#sudo docker run -p 5000:5000 flaskapi:latest