from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_video/<path:filename>')
def get_video(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)