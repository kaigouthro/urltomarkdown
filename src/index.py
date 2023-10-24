   from flask import Flask, request, jsonify
   from flask_limiter import Limiter
   from src import url_to_markdown_readers, url_to_markdown_processor
   from urllib.parse import urlparse
   import os

   app = Flask(__name__)
   limiter = Limiter(app, key_func=get_remote_address)

   @app.route('/', methods=['GET', 'POST'])
   @limiter.limit("5/minute")
   def process_url():
       url = request.args.get('url')
       title = request.args.get('title')
       links = request.args.get('links')
       inline_title = False
       ignore_links = False
       if title:
           inline_title = (title == 'true')
       if links:
           ignore_links = (links == 'false')
       if url and validURL(url):
           read_url(url, inline_title, ignore_links)
       else:
           return jsonify(error="Please specify a valid url query parameter"), 400

   def read_url(url, inline_title, ignore_links):
       reader = url_to_markdown_readers.reader_for_url(url)
       reader.read_url(url, inline_title, ignore_links)

   def validURL(str):
       try:
           result = urlparse(str)
           return all([result.scheme, result.netloc])
       except ValueError:
           return False

   if __name__ == "__main__":
       port = int(os.environ.get("PORT", 5000))
       app.run(host='0.0.0.0', port=port)