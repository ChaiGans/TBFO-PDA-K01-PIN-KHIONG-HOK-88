# main.py

import sys
import re

def print_html_tags_and_text(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(r'\n', '', content)
    result = []
    current_part = ""
    inside_tag = False
    error_space = False
    read_string = False

    for char in content:
        if char == '<':
            if current_part.strip():  # Check if current_part is non-empty and contains non-whitespace characters
                result.append('STR')
            current_part = ""
            result.append('<')  # Add the '<' as a separate item
            inside_tag = True
        elif char == '>':
            if current_part and not error_space:  # Add the current part if it exists
                result.append(current_part)
            elif current_part and error_space: # notvalid condition is when it got front space on the tags
                result.append("notvalid")
            result.append('>')  # Add the '>' as a separate item
            current_part = ""
            inside_tag = False
            error_space = False
        elif inside_tag:
            # print("err", error_space)
            # print("read", read_string)
            if char == '"':
                if (read_string):
                    result.append('X')
                    current_part = ""
                read_string = not read_string 
            if char in [' ', '=', '"']:  # Split on spaces, slashes, and equals within tags
                if current_part == "" and not read_string:
                    error_space = True
                elif current_part and not error_space and not read_string:
                    if (current_part not in ["html", "title", "head", "body", "h1", "h2", "h3", "h4", "h5", "h6", "p", "br", "em", "b", "abbr", "strong", "small", "hr", "div", "table", "tr", "td", "th", "rel", "class", "href", "src", "alt", "type", "action", "method", "GET", "POST", "type", "form", "img", "a", "button", "input", "link", "script"]):
                        result.append('STR')
                    else:
                        result.append(current_part)
                    current_part = ""
                if char=='=' and not read_string:
                    result.append(char)
            else:
                current_part += char
        else:
            current_part += char

    # Add any remaining part
    if current_part:
        result.append(current_part)

    print(result)


if len(sys.argv) != 2:
    print("Usage: python main.py <filename>")
else:
    print_html_tags_and_text(sys.argv[1])