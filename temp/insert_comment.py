# Import the BeautifulSoup library
from bs4 import BeautifulSoup

# Read the comment text from the standard input
comment = input()

# Open the HTML file and parse it with BeautifulSoup
with open('comments.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the comments section in the HTML
comments = soup.find('div', id='comments')

# Create a new div element to hold the comment
comment_div = soup.new_tag('div')
comment_div.string = comment

# Add the comment to the comments section
comments.append(comment_div)

# Save the modified HTML file
with open('comments.html', 'w') as f:
    f.write(str(soup))

