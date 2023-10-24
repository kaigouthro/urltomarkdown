   import re
   from urllib.parse import urlparse

   class url_to_markdown_common_filters:
       def filter(self, url, data, ignore_links=False):
           domain = ''
           base_address = ''
           if url:
               url = urlparse(url)
               if url:
                   base_address = url.scheme + "://" + url.netloc
                   domain = url.netloc

           # make relative URLs absolute
           data = re.sub(r'\[([^\]]*)\]\(\/([^\/][^\)]*)\)', r'[\1](' + base_address + r'/\2)', data)

           # remove inline links and refs
           if ignore_links:
               data = re.sub(r'\[\[?([^\]]+\]?)\]\([^\)]+\)', r'\1', data)
               data = re.sub(r'[\\\[]+([0-9]+)[\\\]]+', r'[\1]', data)

           return data