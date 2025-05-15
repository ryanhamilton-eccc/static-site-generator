import unittest
from markdown_to_html import markdown_to_html_node
from htmlnode import ParentNode, LeafNode
from markdown_to_html import extract_title


class TestMarkdownToHTML(unittest.TestCase):
    def test_heading(self):
        markdown = "# Heading 1"
        html_node = markdown_to_html_node(markdown)
        self.assertIsInstance(html_node, ParentNode)
        self.assertEqual(html_node.children[0].tag, "h1")
        self.assertEqual(html_node.children[0].value, "Heading 1")

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>",
        )

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# This is the title"
        title = extract_title(markdown)
        self.assertEqual(title, "This is the title")

    def test_extract_title_with_multiple_lines(self):
        markdown = """
# This is the title

This is a paragraph.
        """
        title = extract_title(markdown)
        self.assertEqual(title, "This is the title")

    def test_extract_title_no_title(self):
        markdown = """
This is a paragraph.
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()