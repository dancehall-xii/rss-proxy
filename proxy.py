Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, jsonify
... import feedparser
... 
... app = Flask(__name__)
... 
... @app.route("/noticias")
... def noticias():
...     feed = feedparser.parse("https://www.nacion.com/rss/")
...     headlines = [entry.title for entry in feed.entries[:3]]
...     return jsonify({"headlines": headlines})
... 
... if __name__ == "__main__":
...     app.run(host="0.0.0.0", port=5000)
