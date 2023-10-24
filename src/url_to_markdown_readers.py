   from src import url_to_markdown_apple_dev_docs, url_to_markdown_processor
   from bs4 import BeautifulSoup
   import requests

   apple_dev_prefix = "https://developer.apple.com"
   stackoverflow_prefix = "https://stackoverflow.com/questions"

   class html_reader:
       def read_url(self, url, inline_title, ignore_links):
           response = requests.get(url)
           soup = BeautifulSoup(response.text, 'html.parser')
           markdown = url_to_markdown_processor.process_dom(url, soup, inline_title, ignore_links)
           return markdown

   class apple_reader:
       def read_url(self, url, inline_title, ignore_links):
           json_url = url_to_markdown_apple_dev_docs.dev_doc_url(url)
           response = requests.get(json_url)
           json = response.json()
           markdown = url_to_markdown_apple_dev_docs.parse_dev_doc_json(json, inline_title, ignore_links)
           return markdown

   class stack_reader:
       def read_url(self, url, inline_title, ignore_links):
           response = requests.get(url)
           soup = BeautifulSoup(response.text, 'html.parser')
           markdown_q = url_to_markdown_processor.process_dom(url, soup, inline_title, ignore_links, 'question')
           markdown_a = url_to_markdown_processor.process_dom(url, soup, False, ignore_links, 'answers')
           if markdown_a.startswith('Your Answer'):
               return markdown_q
           else:
               return markdown_q + "\n\n## Answer\n"+ markdown_a

   def reader_for_url(url):
       if url.startswith(apple_dev_prefix):
           return apple_reader()
       elif url.startswith(stackoverflow_prefix):
           return stack_reader()
       else:
           return html_reader()

   def ignore_post(url):
       if url and url.startswith(stackoverflow_prefix):
           return True
       else:
           return False