   from html_table_extractor.extractor import Extractor
   from html.parser import HTMLParser
   import re

   class url_to_markdown_formatters:
       def format_tables(self, html, replacements):
           extractor = Extractor(html)
           extractor.parse()
           tables = extractor.return_list()
           for i, table in enumerate(tables):
               markdown = "| " + " | ".join(table[0]) + " |\n"
               markdown += "| " + " | ".join(["---"] * len(table[0])) + " |\n"
               for row in table[1:]:
                   markdown += "| " + " | ".join(row) + " |\n"
               placeholder = "urltomarkdowntableplaceholder" + str(i)
               replacements.append({'placeholder': placeholder, 'replacement': markdown})
               html = html.replace(str(table), placeholder)
           return html

       def format_codeblocks(self, html, replacements):
           codeblocks = re.findall(r'<pre[^>]*>(.*?)</pre>', html, re.DOTALL)
           for i, codeblock in enumerate(codeblocks):
               codeblock = HTMLParser().unescape(codeblock)