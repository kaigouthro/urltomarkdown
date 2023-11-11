   from src import url_to_markdown_formatters, url_to_markdown_common_filters
   from readability import Document
   import markdownify

   def process_dom(url, document, inline_title, ignore_links, id=""):
       title = document.title
       if id:
           document = BeautifulSoup(
               document.select_one(f"#{id}").prettify(), 'html.parser'
           )
       readable = Document(str(document)).summary()
       replacements = []
       readable = url_to_markdown_formatters.format_codeblocks(readable, replacements)
       readable = url_to_markdown_formatters.format_tables(readable, replacements)
       markdown = markdownify.markdownify(readable)
       for replacement in replacements:
           markdown = markdown.replace(replacement['placeholder'], replacement['replacement'])
       result = url_to_markdown_common_filters.filter(url, markdown, ignore_links) if url else markdown
       if inline_title and title:
           result = f"# {title}" + "\n" + result
       return result