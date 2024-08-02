from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# Path to the text file
TEXT_FILE_PATH = '/Users/micahlai/Documents/Github/display-log/test.txt'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/content')
def get_content():
    try:
        with open(TEXT_FILE_PATH, 'r') as file:
            content = file.read()
        return jsonify(content)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)