from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

all_articles = []
liked_articles = []
not_liked_articles = []

with open("d1_nona.csv", encoding="UTF-8") as f:
    
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

@app.route("/get-article")
def get_article():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    })

@app.route("/disliked-article", methods=["POST"])
def disliked_article():
    
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    })


if(__name__ == "__main__"):
    app.run()
    
