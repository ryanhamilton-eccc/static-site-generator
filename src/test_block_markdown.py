import unittest
from markdown_blocks import markdow_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_heading(self):
        markdown = "# This is a heading"
        blocks = markdow_to_blocks(markdown)
        self.assertEqual(blocks, ["# This is a heading"])

    def test_paragraph(self):
        markdown = "This is a paragraph of text."
        blocks = markdow_to_blocks(markdown)
        self.assertEqual(blocks, ["This is a paragraph of text."])

    def test_list(self):
        markdown = "* Item 1\n* Item 2\n* Item 3"
        blocks = markdow_to_blocks(markdown)
        self.assertEqual(blocks, ["* Item 1\n* Item 2\n* Item 3"])

    def test_multiple_blocks(self):
        markdown = "# Heading\n\nThis is a paragraph.\n\n* Item 1\n* Item 2"
        blocks = markdow_to_blocks(markdown)
        self.assertEqual(blocks, ["# Heading", "This is a paragraph.", "* Item 1\n* Item 2"])

    def test_empty_lines(self):
        markdown = "\n\n# Heading\n\n\nThis is a paragraph.\n\n\n* Item 1\n* Item 2\n\n"
        blocks = markdow_to_blocks(markdown)
        self.assertEqual(blocks, ["# Heading", "This is a paragraph.", "* Item 1\n* Item 2"])

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_code_block(self):
        block = "```\nprint('Hello, world!')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "code")

    def test_quote_block(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")

    def test_paragraph_block(self):
        block = "This is a paragraph."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_empty_block(self):
        block = ""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_multiline_quote_block(self):
        block = "> This is a quote\n> that spans multiple lines."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")

    def test_unordered_list_block(self):
        block = "* Item 1\n* Item 2\n* Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered_list")

    def test_ordered_list_block(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "ordered_list")

    def test_invalid_ordered_list_block(self):
        block = "1. Item 1\n3. Item 2\n2. Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

if __name__ == "__main__":
    unittest.main()