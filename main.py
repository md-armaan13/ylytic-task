import awsgi
from flask import Flask ,Response, request, jsonify
from flask_restful import Api 
import requests
from datetime import datetime
from views import filter_comments


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Hello World"

@app.route('/search', methods=['GET'])
def search_comments():

    try:
        response = requests.get("https://app.ylytic.com/ylytic/test")
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch comments from the external API"}), response.status_code
        comments = response.json().get('comments', [])
    except ValueError:
        return jsonify({"error": "Failed to parse JSON from the external API response"}), 500
    
    search_author = request.args.get('search_author', None)
    at_from = request.args.get('at_from', None)
    at_to = request.args.get('at_to', None)
    like_from = request.args.get('like_from', None)
    like_to = request.args.get('like_to', None)
    reply_from = request.args.get('reply_from', None)
    reply_to = request.args.get('reply_to', None)
    search_text = request.args.get('search_text', None)
    results = filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text)

    return jsonify({"comments": results})

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == "__main__":
    app.run(debug=True)
    

