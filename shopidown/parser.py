# coding: utf-8

import re

# Guillaume:
#
# I'm using more comments here to make easier to
# follow what I'm doing in Python, in real life code
# I would not comment the obvious things.
#
# Also, it runs fine on python 2.7, python 3.5 and
# on Pypy.


def parse_styles(text):
    """ Parse styles into html """

    # Style regex (finally made the regex work, phew)
    # Big thanks to the Patterns macOS app, because it
    # helps to see if the regex is really doing what it
    # is intented to do.
    bold = re.compile("\\*{2}([a-z]+)\\*{2}", re.UNICODE)
    italic = re.compile("\\*{1}([a-z]+)\\*{1}", re.UNICODE)

    # Replace bold for <strong> and </strong>
    parsed_text = bold.sub(r"<strong>\1</strong>", text)

    # Replace italic for <em> and </em>
    parsed_text = italic.sub(r"<em>\1</em>", parsed_text)

    return parsed_text


class Parser(object):
    """ Simple markdown parser """

    def __init__(self):
        super(Parser, self).__init__()

        # The lists to accumulate the ordered and
        # unordered items
        self.unordered_items = []
        self.ordered_items = []
        self.multiline = False

    def parse_list_items(self):
        """ Parse the collected list items """

        html = []

        if self.unordered_items:
            html.append("<ul>\n")

            for item in self.unordered_items:
                html.append("  <li>%s</li>\n" % item.replace("- ", "", 1))

            html.append("</ul>\n")

            # Lets empty the unordered items list
            self.unordered_items = []

        if self.ordered_items:
            html.append("<ol>\n")

            for item in self.ordered_items:
                html.append("  <li>%s</li>\n" % re.sub("^[1-9]\\. ", "", item))

            html.append("</ol>\n")

            # Lets empty the unordered items list
            self.ordered_items = []

        return "".join(html)

    def handle_multiline(self, text):
        """
        If the input text is a multiline string we
        need to add a \n to the end of the text
        """

        if self.multiline is True:
            return "%s\n" % text
        else:
            return text

    def parse(self, text):
        """ Parse markdown text into html """

        lines = text.splitlines()
        html = []

        if len(lines) > 1:
            self.multiline = True

        for line in lines:
            if line.startswith("# "):  # Title
                new_line = "<h1>%s</h1>" % line.replace("# ", "", 1)
                new_line = self.handle_multiline(new_line)
                html.append(new_line)
                continue
            elif line.startswith("## "):  # Subtitle
                new_line = "<h2>%s</h2>" % line.replace("## ", "", 1)
                new_line = self.handle_multiline(new_line)
                html.append(new_line)
                continue
            elif line.startswith("- "):  # Unordered item
                self.unordered_items.append(line)
                continue
            elif re.search("^[1-9]\\. ", line):  # Ordered item
                self.ordered_items.append(line)
                continue

            # Lets see if we have to create the ul or ol tree
            html.append(self.parse_list_items())

            if not line:
                html.append("\n")
            else:
                # Paragraph
                new_line = self.handle_multiline("<p>%s</p>" % line)
                html.append(new_line)

        # If we just had lists on our text we need to
        # process them after the loop
        if self.unordered_items:
            html.append(self.parse_list_items())
        elif self.ordered_items:
            html.append(self.parse_list_items())

        # Now we will transform the html tokens in
        # html text
        html_text = "".join(html)

        # To finish, lets parse the styles =)
        return parse_styles(html_text)
