from flask import Flask, request, jsonify, redirect, url_for, render_template
from werkzeug.utils import secure_filename
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

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route("/upload", methods=["POST"])
def upload_file():
    f = request.files['file']
    if f.filename != '':  
        f.save(secure_filename(f.filename))
    return redirect(url_for('display_analytics'))

@app.route("/analytics")
def display_analytics():
    return render_template('display_analytics.html')

#def count_words():


if __name__ == "__main__":
    app.run(debug=True)

#sudo docker build -t flaskapi:latest .
#sudo docker run -p 5000:5000 flaskapi:latest

#sudo docker-compose build
#sudo docker-compose up