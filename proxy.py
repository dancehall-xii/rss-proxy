from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

@app.route("/noticias")
def noticias():
    feeds = {
        "La Nación": "https://www.nacion.com/rss/",
        "BBC Mundo": "https://feeds.bbci.co.uk/mundo/rss.xml",
        "CNN en Español": "http://rss.cnn.com/rss/edition_espanol.rss"
    }

    all_headlines = {}

    for name, url in feeds.items():
        try:
            feed = feedparser.parse(url)
            if feed.bozo:  # error al parsear
                all_headlines[name] = ["Error al leer feed"]
            else:
                headlines = [entry.title for entry in feed.entries[:3]]
                if headlines:
                    all_headlines[name] = headlines
                else:
                    all_headlines[name] = ["Sin titulares disponibles"]
        except Exception as e:
            all_headlines[name] = [f"Error: {str(e)}"]

    return jsonify(all_headlines)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
