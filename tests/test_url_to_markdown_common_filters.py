   import unittest
   from src import url_to_markdown_common_filters

   class TestUrlToMarkdownCommonFilters(unittest.TestCase):
       def test_filter(self):
           test_markdown = "![photo](https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/photo.svg/20px-photo.svg.png)"
           expected_markdown = "![photo](https://upload.wikimedia.org/wikipedia/en/1/1b/photo.svg)"
           filtered_markdown = url_to_markdown_common_filters.filter("https://en.wikipedia.org/wiki/test", test_markdown)
           self.assertEqual(filtered_markdown, expected_markdown)

   if __name__ == '__main__':
       unittest.main()