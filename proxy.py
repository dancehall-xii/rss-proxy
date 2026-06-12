from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

@app.route("/noticias")
def noticias():
    feeds = {
        "La Nación": "https://www.nacion.com/rss/",
        "CRHoy": "https://www.crhoy.com/feed/",
        "Diario Extra": "https://www.diarioextra.com/rss"
    }

    all_headlines = {}

    for name, url in feeds.items():
        feed = feedparser.parse(url)
        headlines = [entry.title for entry in feed.entries[:3]]
        all_headlines[name] = headlines

    return jsonify(all_headlines)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
