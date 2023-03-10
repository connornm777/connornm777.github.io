# After editing the menu block just run: python3 menu.py
# to update the menu
import os
import re

# Define regular expression pattern to match button tags
pattern = r'<!--begin menu-->[\s\S]*?<!--end menu-->'

# Write the actual menu here
menu = """
<!--begin menu-->
<button><a href="index.html">Home</a></button>
<button><a href="bookreviews.html">Book Reviews</a></button>
<button><a href="physics.html">Physics</a></button>
<button><a href="games.html">Games</a></button>
<button><a href="misc.html">Misc</a></button>
<!--end menu-->
"""

# Loop through all HTML files in the current directory
for filename in os.listdir():
    if filename.endswith('.html'):
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the file contents
            content = file.read()
            # Use regular expressions to find and remove all button tags
            content = re.sub(pattern, menu, content)
            # Remove any extra vertical whitespace at the end of the file
            content=re.sub(r"^\s+", "", content, flags = re.MULTILINE)
            content += "\n"
        # Open the file for writing and overwrite the old contents
        with open(filename, 'w') as file:
            file.write(content)
