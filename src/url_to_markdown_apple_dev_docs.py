   import requests
   from urllib.parse import urlparse, urljoin

   class url_to_markdown_apple_dev_docs:
       def dev_doc_url(self, url):
           query_parts = url.split('?')
           queryless = query_parts[0]
           if queryless.endswith('/'):
               queryless = queryless[:-1]
           parts = queryless.split("/")
           json_url = "https://developer.apple.com/tutorials/data"
           for part in parts[3:]:
               json_url = urljoin(json_url, part)
           json_url += ".json"
           return json_url

       def parse_dev_doc_json(self, json, inline_title=True, ignore_links=False):
           text = ""
           if inline_title and 'metadata' in json and 'title' in json['metadata']:
               text += "# " + json['metadata']['title'] + "\n\n"
           if 'references' in json:
               self.dev_references = json['references']
           if 'primaryContentSections' in json:
               text += self.process_sections(json['primaryContentSections'], ignore_links)
           elif 'sections' in json:
               text += self.process_sections(json['sections'], ignore_links)
           return text

       def process_sections(self, sections, ignore_links):
           text = ""
           for section in sections:
               if 'kind' in section:
                   if section['kind'] == 'declarations' and 'declarations' in section:
                       for declaration in section['declarations']:
                           if 'tokens' in declaration:
                               token_text = "".join(token['text'] for token in declaration['tokens'])
                               text += token_text
                           if 'languages' in declaration and declaration['languages']:
                               language_text = "\nLanguages: " + ", ".join(declaration['languages'])
                               text += f" {language_text}"
                           if 'platforms' in declaration and declaration['platforms']:
                               platform_text = "\nPlatforms: " + ", ".join(declaration['platforms'])
                               text += f" {platform_text}"
                       text += "\n\n"
                   elif section['kind'] == 'content':
                       text += self.process_content_section(section, ignore_links)
               if 'title' in section:
                   if 'kind' in section and section['kind'] == 'hero':
                       text += "# " + section['title'] + "\n"
                   else:
                       text += "## " + section['title']
               if 'content' in section:
                   for sectionContent in section['content']:
                       if 'type' in sectionContent and sectionContent['type'] == 'text':
                           text += sectionContent['text'] + "\n"
           return text

       def process_content_section(self, section, ignore_links):
           text = ""
           for content in section['content']:
               if 'type' in content:
                   if content['type'] == 'paragraph' and 'inlineContent' in content:
                       inline_text = ""
                       for inline in content['inlineContent']:
                           if 'type' in inline:
                               if inline['type'] == "text":
                                   inline_text += inline['text']
                               elif inline['type'] == "link":
                                   if ignore_links:
                                       inline_text += inline['title']
                                   else:
                                       inline_text += "[" + inline['title'] + "](" + inline['destination'] + ")"
                               elif inline['type'] == "reference" and 'identifier' in inline and inline['identifier'] in self.dev_references:
                                   inline_text += self.dev_references[inline['identifier']]['title']
                               elif inline['type'] == 'codeVoice' and 'code' in inline:
                                   inline_text += "`" + inline['code'] + "`"
                       text += inline_text + "\n\n"
                   elif content['type'] == 'codeListing':