# extract multiple times a substring with the same repeating bracketing substrings

import sys
import re
'''# for 1 instance of extraction
text = 'Some HTML text here View course details for Intro to Python" onClick="someFunction()'

# Define your substrings (with raw strings)
sub_bracket_start = r'View course details for '
sub_bracket_end = r'" onClick='

# Match everything between sub_bracket_start and sub_bracket_end
brackets_and_subtext = re.search(f'{sub_bracket_start}(.*?){sub_bracket_end}', text) # Utilizing .*? ensures a "non-greedy" match so it grabs only the text directly between the nearest markers.

if brackets_and_subtext:
    subtext = brackets_and_subtext.group(1) # not sure what the .group() method does.
    print(subtext)  # Output: Intro to Python
    print(brackets_and_subtext) # <re.Match object; span=(20, 69) (indexes start and end in the variable text), match='View course details for Intro to Python" onClick=>
'''

# To extract multiple times same subtext
'''
text = """
<a href="#" View course details for Intro to Python" onClick="f()">...</a>
<a href="#" View course details for Advanced Data Science" onClick="f()">...</a>
<a href="#" View course details for Web Development" onClick="f()">...</a>
"""

text_single_instance = 'Some HTML text here View course details for Intro to Python" onClick="someFunction()'

# Define pattern with a non-greedy capture group (.*?)
pattern = r'View course details for (.*?)" onClick='

# Extract all matches into a list
courses = re.findall(pattern, text)
courses2 = re.findall(pattern, text_single_instance)

print(courses)
# Output: ['Intro to Python', 'Advanced Data Science', 'Web Development']
print(courses2)
# Output: ['Intro to Python']
'''

def extract_multiple_bracketed_subtext(pattern, text):
    '''
    Extract subtexts from bracketed string patterns multiple times.
    Need re module imported.

    Parameters:
    pattern: raw string with 'starting_bracketing_substring (.*?) ending_bracketing_substring';
        Example: r'View course details for (.*?)" onClick='
    text: string of entire text to extract from.

    Return list of strings that were extracted.
    '''

    extracted_strings = re.findall(pattern, text)

    return extracted_strings


if __name__ == '__main__':
    # sys.argv[0] is always the script name itself
    # Check if the user provided the required argument
    if len(sys.argv) > 1:
        user_argument = sys.argv[1]
        # 'main' function call
        extract_multiple_bracketed_subtext(user_argument)
    else: 
        print("Error: Please provide the required argument.")
