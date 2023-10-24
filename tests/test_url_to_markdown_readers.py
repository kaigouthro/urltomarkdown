   import unittest
   from src import url_to_markdown_readers

   class TestUrlToMarkdownReaders(unittest.TestCase):
       def test_get_html_reader(self):
           reader = url_to_markdown_readers.reader_for_url("https://en.wikipedia.org")
           self.assertIsInstance(reader, url_to_markdown_readers.html_reader)

       def test_get_stack_overflow_reader(self):
           reader = url_to_markdown_readers.reader_for_url("https://stackoverflow.com/questions/0")
           self.assertIsInstance(reader, url_to_markdown_readers.stack_reader)

       def test_get_apple_dev_docs_reader(self):
           reader = url_to_markdown_readers.reader_for_url("https://developer.apple.com/documentation/swift/array")
           self.assertIsInstance(reader, url_to_markdown_readers.apple_reader)

   if __name__ == '__main__':
       unittest.main()