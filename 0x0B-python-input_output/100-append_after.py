#!/usr/bin/python3
"""
    Module with function that reads file and
    appends given string after a specified
    string
"""


def append_after(filename="", search_string="", new_string=""):
    """function that reads file, appending new_string after
    search string
    """
    with open(filename, 'r+') as f:
        fcontent = f.read()
        new_content = ""
        for line in fcontent.splitlines():
            if search_string in line:
                new_content += line + "\n" + new_string
            else:
                new_content += line + "\n"

        f.seek(0)
        f.truncate()
        f.write(new_content)
