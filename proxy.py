from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

@app.route("/noticias")
def noticias():
    feed = feedparser.parse("https://www.nacion.com/rss/")
    headlines = [entry.title for entry in feed.entries[:3]]
    return jsonify({"headlines": headlines})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
