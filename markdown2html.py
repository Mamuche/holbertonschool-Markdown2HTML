#!/usr/bin/python3

""" Markdown to HTML """

import sys
import os


def markdown_to_html(markdown_file, html_file):
    """ function to convert markdown to html """

    html_lines = []

    # open and read markdown file
    with open(markdown_file, "r") as md_file:
        lines = md_file.readlines()

    # go through each line and check if it's one:
    for line in lines:
        # level 1 header
        if line.startswith('# '):
            # add an h1 tag
            html_lines.append(f'<h1>{line[2:]}</h1>')
        # level 2 header
        elif line.startswith('## '):
            # add an h2 tag
            html_lines.append(f'<h2>{line[3:]}</h2>')
        # level 3 header
        elif line.startswith('### '):
            # add an h3 tag
            html_lines.append(f'<h3>{line[4:]}</h3>')
        # level 4 header
        elif line.startswith('#### '):
            # add an h4 tag
            html_lines.append(f'<h4>{line[5:]}</h4>')
        # level 5 header
        elif line.startswith('##### '):
            # add an h5 tag
            html_lines.append(f'<h5>{line[6:]}</h5>')
        # level 6 header
        elif line.startswith('###### '):
            # add an h6 tag
            html_lines.append(f'<h6>{line[7:]}</h6>')
        # if it's a list
        elif line.startswith('- '):
            # check if one is already open
            if not html_lines or not html_lines[-1].startswith('<ul>'):
                # add the lu tag
                html_lines.append('<ul>')
            # add the li tag
            html_lines.append(f'<li>{line[2:]}</li>')
            # verifies if this is the end of the list
            # if (len(lines) == lines.index(line) + 1 or
            # not lines[lines.index(line) + 1].startswith('- ')):
            # close the list
            html_lines.append('</ul>')
        else:
            # add a p tag if it's not a header or a list or an empty line
            if line.strip():
                html_lines.append(f'<p>{line}</p>')

    html_content = '\n'.join(html_lines)

    # open and write to html file
    with open(html_file, "w") as hl_file:
        hl_file.write(html_content)


def main():
    # check number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # check if markdown exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # convert markdown to html
    markdown_to_html(markdown_file, html_file)


if __name__ == "__main__":
    main()
