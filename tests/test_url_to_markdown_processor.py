   import unittest
   from src import url_to_markdown_processor
   from bs4 import BeautifulSoup

   class TestUrlToMarkdownProcessor(unittest.TestCase):
       def test_process_html(self):
           test_html_document = "<html><head><title>test page</title></head><body><p>first paragraph</p><h2>heading 2</h2><p>second paragraph</p><h3>heading 3</h3><p>third paragraph</p><p><em>italics</em> <strong>bold</strong></p><p><a href='http://some.url/link'>link</a></p><p><img alt='photo' src='http://some.url/img'></img></p></body></html>"
           expected_markdown_output = "# test page\nfirst paragraph\n\nheading 2\n---------\n\nsecond paragraph\n\n### heading 3\n\nthird paragraph\n\n_italics_ **bold**\n\n[link](http://some.url/link)\n\n![photo](http://some.url/img)"
           soup = BeautifulSoup(test_html_document, 'html.parser')
           actual_markdown_output = url_to_markdown_processor.process_dom("http://some.url", soup, True, False)
           self.assertEqual(actual_markdown_output, expected_markdown_output)

   if __name__ == '__main__':
       unittest.main()