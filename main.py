import sys
import re
from pda import *

def print_html_tags_and_text(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # content = re.sub(r'\n', '', content)
    result = []
    current_part = ""
    inside_tag = False
    error_space = False
    read_string = False
    in_comment = False
    in_form_tag = False
    in_input_tag = False
    in_button_tag = False
    in_method_attribute = False
    in_type_attribute = False
    in_button_attribute = False
    reading_space_between = False
    reading_space_between_input = False
    reading_space_between_form = False
    line_number = 1
    
    valid_tags = ["html", "title", "head", "body", "h1", "h2", "h3", "h4", "h5", "h6", "p", "br", "em", "b", "abbr", "strong", "small", "hr", "div", "table", "tr", "td", "th", "rel", "class", "href", "src", "alt", "type", "action", "method", "GET", "POST", "type", "form", "img", "a", "button", "input", "link", "script", "!--"]

    i = 0
    while i < len(content):
        char = content[i]
        # print("Current Part:", current_part)
        # print(result)

        if char == '\n':
            line_number += 1

        if char == '<':
            if current_part.strip() and not inside_tag:
                result.append(["STR",line_number])
            elif in_comment:
                result.append(["STR",line_number])
            current_part = '<'
            inside_tag = True
            error_space = False

            if inside_tag and current_part == '<' and content.startswith('form', i + 1):
                in_form_tag = True
            elif inside_tag and current_part == '<' and content.startswith('/form', i + 1):
                in_form_tag = False

            if inside_tag and current_part == '<' and content.startswith('input', i + 1):
                in_input_tag = True
            elif inside_tag and current_part == '<' and content.startswith('/input', i + 1):
                in_input_tag = False

            if inside_tag and current_part == '<' and content.startswith('button', i + 1):
                in_button_tag = True
            elif inside_tag and current_part == '<' and content.startswith('/button', i + 1):
                in_button_tag = False


            if content[i+1:i+2] == '/':
                slash_index = i + 2  # Start after '</'
                tag_end = content.find('>', slash_index)
                if tag_end == -1:
                    error_space = True
                else:
                    # Extract tag name, excluding any trailing spaces
                    tag_name_end = content.find(' ', slash_index)
                    if tag_name_end == -1 or tag_name_end > tag_end:
                        tag_name_end = tag_end
                    tag_name = content[slash_index:tag_name_end]

                    # Check if the tag name is valid and there are no spaces within it
                    if ' ' in tag_name or tag_name not in valid_tags:
                        error_space = True
                    else:
                        current_part += '/' + tag_name
                        i = tag_end - 1             
            
            
            if not error_space:
                if content[i:i+4] == '<!--':
                    comment_end = content.find('-->', i)
                    if comment_end != -1:
                        result.append(['!--',line_number])
                        # Append everything inside the comment as 'STR'
                        result.append(['STR',line_number])
                        result.append(['-->',line_number])
                        i = comment_end + 3  # Skip to the end of the comment
                        current_part=""
                        inside_tag = False
                        continue
                    else:
                        error_space = True

                tag_found = False
                comment_found = False
                tag_len = content.find('>', i) - (i + 1)
                for tag in valid_tags:
                    tag_len = len(tag)
                    if content[i+1:i+1+tag_len] == tag and (i+1+tag_len == len(content) or not content[i+1+tag_len].isalpha()):
                        current_part += tag
                        i += tag_len  # Skip the characters of the tag
                        tag_found = True
                        break

                if not tag_found:
                    # Check for space within the tag name
                    tag_end = content.find('>', i)
                    if ' ' in content[i+1:tag_end]:
                        error_space = True

                if tag_found or comment_found:
                    result.append([current_part.strip(), line_number])
                    current_part = ""
                    inside_tag = True
                    in_comment = comment_found   
                else:
                    inside_tag = True
        elif char == '=' and in_form_tag:
            if in_form_tag:
                if current_part == 'method':
                    in_method_attribute = True
                else:
                    in_method_attribute = False
            if not read_string:
                result.append([current_part.strip(), line_number])
                result.append([char.strip(), line_number])
                current_part = ""
            else:
                current_part += char
        elif char == '"' and in_form_tag:
            if read_string :
                if in_method_attribute and current_part in ['GET', 'POST','get','post'] and ' ' not in current_part :
                    result.append(['X',line_number])
                elif not in_method_attribute:
                    result.append(['X',line_number])
                in_method_attribute = False
                reading_space_between_form = False
                current_part = ""
            else:
                current_part=""
                if in_method_attribute:
                    reading_space_between_form = True
            read_string = not read_string
        elif char == '=' and in_input_tag:
            if in_input_tag :
                if current_part == 'type':
                    in_type_attribute = True
                else :
                    in_type_attribute = False 
            if not read_string:
                result.append([current_part.strip(), line_number])
                result.append([char.strip(), line_number])
                current_part = ""
            else:
                current_part += char
        elif char == '"' and in_input_tag:
            if read_string:
                if in_type_attribute and current_part in ['text', 'password','email','number','checkbox'] and ' ' not in current_part :
                        result.append(['X',line_number])
                elif not in_method_attribute:
                    result.append(['X',line_number])                        
                in_type_attribute = False
                reading_space_between_input = False
                current_part = ""
            else:
                current_part=""
                if in_type_attribute:
                    reading_space_between_input = True
            read_string = not read_string
        elif char == '=' and in_button_tag:
            if in_button_tag :
                if current_part == 'type':
                    in_button_attribute = True 
                else:
                    in_button_attribute = False 
            if not read_string:
                result.append([current_part.strip(), line_number])
                result.append([char.strip(), line_number])
                current_part = ""
            else:
                current_part += char
        elif char == '"' and in_button_tag:
            if read_string:
                if in_button_attribute and current_part in ['submit','reset','button'] and ' ' not in current_part :
                        result.append(['X',line_number])
                elif not in_button_attribute:
                    result.append(['X',line_number])                        
                in_button_attribute = False
                reading_space_between = False
                current_part = ""
            else:
                current_part=""
                if in_button_attribute:
                    reading_space_between = True
            read_string = not read_string
        elif read_string and reading_space_between:
            current_part += char
        elif read_string and reading_space_between_input:
            current_part += char
        elif read_string and reading_space_between_form:
            current_part += char
        elif char == '>':
            if current_part and not error_space:  # Add the current part if it exists
                result.append([current_part.strip(), line_number])
            elif current_part and error_space:  # notvalid condition is when it got front space on the tags
                result.append(["notvalid",line_number])
            result.append([">", line_number])  # Add the '>' as a separate item
            current_part = ""
            inside_tag = False
            in_form_tag = False
            in_button_tag = False
            in_input_tag = False
            error_space = False
            in_comment = False
        elif inside_tag:
            if char == '"':
                if read_string:
                    result.append(["X", line_number])
                    current_part = ""
                read_string = not read_string
            if char == ' ' and current_part == "<":
                error_space = True
            elif char in [' ', '=', '"']:  # Split on spaces, slashes, and equals within tags
                if current_part == "" and not read_string:
                    error_space = True
                elif current_part and not error_space and not read_string:
                    if (current_part not in valid_tags):
                        result.append(['STR',line_number])
                    current_part = ""
                if char=='=' and not read_string:
                    result.append([current_part.strip(), line_number])
                    result.append([char.strip(), line_number])
                    current_part = ""
            else:
                current_part += char
        else:
            current_part += char

        i += 1

    # Add any remaining part
    if current_part:
        result.append([current_part.strip(), line_number])
    result = [item for item in result if not (isinstance(item[0], str) and item[0].isspace() and item[0] != 'STR')]
    # print(result)
    return result




if len(sys.argv) != 3:
    print("Usage: python main.py <'file'.txt> <'file'.html>")
else:
    tokens=print_html_tags_and_text(sys.argv[2])
    thepda=bacapda(sys.argv[1])
    processingpda(thepda,tokens)

# hasil = print_html_tags_and_text("tes.html")
# print("ini hasil",hasil)
