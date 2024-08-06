#!/usr/bin/python3

import sys
import os

def markdown_to_html(markdown_file, html_file):
    """ function to convert markdown to html """

    html_lines = []

    #open markdown file
    with open(markdown_file, "r") as md_file:
        lines = md_file.readlines()
    

    for line in lines:
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('- '):
            if not html_lines or not html_lines[-1].startswith('<ul>'):
                html_lines.append('<ul>')
            html_lines.append(f'<li>{line[2:]}</li>')
            if len(lines) == lines.index(line) + 1 or not lines[lines.index(line) + 1].startswith('- '):
                html_lines.append('</ul>')
        else:
            html_lines.append(f'<p>{line}</p>')

    html_content = '\n'.join(html_lines)

    with open(html_file, "w") as hl_file:
        hl_file.write(html_content)


def main():
    # check number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
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
