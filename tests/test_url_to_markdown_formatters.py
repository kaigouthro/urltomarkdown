    import unittest
    from src import url_to_markdown_formatters

    class TestUrlToMarkdownFormatters(unittest.TestCase):
        def test_format_table(self):
            test_html_table = "<html><body><table><tr><td>One</td><td>Two</td></tr><tr><td>1</td><td>2</td></tr></table></body></html>"
            expected_markdown_table = "| One | Two |\n| --- | --- |\n| 1 | 2 |\n"
            replacements = []
            url_to_markdown_formatters.format_tables(test_html_table, replacements)
            output_markdown_table = replacements[0]['replacement']
            self.assertEqual(output_markdown_table, expected_markdown_table)

        def test_format_code_block(self):
            test_html_codeblock = "<html><body><pre><code>#include &lt;stdio.h&gt;\nint main() {\n\tprintf(\"hello world\");\n}</code></pre></body></html>"