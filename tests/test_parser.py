# coding: utf-8

"""
test_shopidown
----------------------------------

Tests for `shopidown` module.
"""

import textwrap


from shopidown.parser import Parser


parser = Parser()

def test_title():
    """ Tests that a title parsers to h1 tag """

    assert parser.parse("# Title *italic* **bold**") == "<h1>Title <em>italic</em> <strong>bold</strong></h1>"

def test_invalid_em_title():
    """
    Tests that a title without two 'em' marks
    parsers to h1 tag
    """

    assert parser.parse("# Title *italic **bold**") == "<h1>Title *italic <strong>bold</strong></h1>"

def test_invalid_strong_title():
    """
    Tests that a title without two 'strong' marks
    parsers to h1 tag
    """

    assert parser.parse("# Title *italic* **bold") == "<h1>Title <em>italic</em> **bold</h1>"

def test_subtitle():
    """ Tests that a subtitle parsers to h2 tags """

    assert parser.parse("## Subtitle") == "<h2>Subtitle</h2>"

def test_pseudo_subtitle():
    """ Tests that a pseudo subtitle parsers to a paragraph """

    assert parser.parse("Subtitle## ") == "<p>Subtitle## </p>"


def test_parse_unordered_list():
    """ Tests that we can parse an unordered list """

    input_text = textwrap.dedent("""\
    - list item 1
    - list item 2
    """)

    output_text = textwrap.dedent("""\
    <ul>
      <li>list item 1</li>
      <li>list item 2</li>
    </ul>
    """)

    assert parser.parse(input_text) == output_text

def test_parse_ordered_list():
    """ Tests that we can parse an ordered list """

    input_text = textwrap.dedent("""\
    1. ordered item 1
    2. ordered item 2
    """)

    output_text = textwrap.dedent("""\
    <ol>
      <li>ordered item 1</li>
      <li>ordered item 2</li>
    </ol>
    """)

    assert parser.parse(input_text) == output_text


def test_lists():
    """ Test that we can parse ul and ol """

    input_text = textwrap.dedent("""\
    - list item 1
    - list item 2

    1. ordered item 1
    2. ordered item 2
    """)

    output_text = textwrap.dedent("""\
    <ul>
      <li>list item 1</li>
      <li>list item 2</li>
    </ul>

    <ol>
      <li>ordered item 1</li>
      <li>ordered item 2</li>
    </ol>
    """)

    assert parser.parse(input_text) == output_text

def test_inverted_lists():
    """ Test that we can parse ol and ul """

    input_text = textwrap.dedent("""\
    1. ordered item 1
    2. ordered item 2

    - list item 1
    - list item 2
    """)

    output_text = textwrap.dedent("""\
    <ol>
      <li>ordered item 1</li>
      <li>ordered item 2</li>
    </ol>

    <ul>
      <li>list item 1</li>
      <li>list item 2</li>
    </ul>
    """)

    assert parser.parse(input_text) == output_text

def test_guilhaume_markdown_text():
    """ Test that we can parse the markdown text Guillaume wrote """

    input_text = textwrap.dedent("""\
    # Title *italic* **bold**

    ## Subtitle

    Paragraph1

    Paragraph2

    - list item 1
    - list item 2

    1. ordered item 1
    2. ordered item 2
    """)

    output_text = textwrap.dedent("""\
    <h1>Title <em>italic</em> <strong>bold</strong></h1>

    <h2>Subtitle</h2>

    <p>Paragraph1</p>

    <p>Paragraph2</p>

    <ul>
      <li>list item 1</li>
      <li>list item 2</li>
    </ul>

    <ol>
      <li>ordered item 1</li>
      <li>ordered item 2</li>
    </ol>
    """)

    assert parser.parse(input_text) == output_text

def test_improved_guilhaume_markdown_text():
    """
    Test that we can parse an improved version of
    the markdown text Guillaume wrote
    """

    input_text = textwrap.dedent("""\
    # Title *italic* **bold**

    ## Subtitle

    Paragraph1

    Paragraph2

    - list item 1
    - list item 2

    1. ordered item 1
    2. ordered item 2

    ## Subtitle

    Paragraph1

    Paragraph2

    # Title *italic* **bold**

    1. ordered item 1
    2. ordered item 2
    3. ordered item 3
    4. ordered item 4

    - list item 1
    - list item 2
    - list item 3
    - list item 4
    """)

    output_text = textwrap.dedent("""\
    <h1>Title <em>italic</em> <strong>bold</strong></h1>

    <h2>Subtitle</h2>

    <p>Paragraph1</p>

    <p>Paragraph2</p>

    <ul>
      <li>list item 1</li>
      <li>list item 2</li>
    </ul>

    <ol>
      <li>ordered item 1</li>
      <li>ordered item 2</li>
    </ol>

    <h2>Subtitle</h2>

    <p>Paragraph1</p>

    <p>Paragraph2</p>

    <h1>Title <em>italic</em> <strong>bold</strong></h1>

    <ol>
      <li>ordered item 1</li>
      <li>ordered item 2</li>
      <li>ordered item 3</li>
      <li>ordered item 4</li>
    </ol>

    <ul>
      <li>list item 1</li>
      <li>list item 2</li>
      <li>list item 3</li>
      <li>list item 4</li>
    </ul>
    """)

    assert parser.parse(input_text) == output_text
