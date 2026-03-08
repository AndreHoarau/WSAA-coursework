from flask import Flask
import json
app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
    return "hello"

@app.route("/fish", methods = ['GET'])
def getall():
    file_path = 'fish.json'
    with open (file_path) as f:
        data = json.load(f)
    return data

@app.route("/fish/<int:id>", methods = ['GET'])
def findbyid(id):
    file_path = 'fish.json'
    with open (file_path) as f:
        data = json.load(f)
        for fish in data["fish"]:
            if fish ["id"] == id:
                return fish
        return f'Error fish {id} not found',404

'''@app.route("/fish", methods = ['GET'])
def getall():
    file_path = 'fish.json'
    with open (file_path) as f:
        data = json.load(f)
    return data
'''
'''@app.route("/fish", methods = ['GET'])
def getall():
    file_path = 'fish.json'
    with open (file_path) as f:
        data = json.load(f)
    return data

@app.route("/fish", methods = ['GET'])
def getall():
    file_path = 'fish.json'
    with open (file_path) as f:
        data = json.load(f)
    return data'''

if __name__ == "__main__":
    app.run(debug=True)


