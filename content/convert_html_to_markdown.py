import os
import html2text

# Set the directory containing the HTML files
html_dir = 'html_dir/'

# Set the directory where the Markdown files will be saved
markdown_dir = 'markdown_dir/'

# Create the directory for the Markdown files if it doesn't exist
if not os.path.exists(markdown_dir):
    os.makedirs(markdown_dir)

# Iterate through each HTML file in the directory
for filename in os.listdir(html_dir):
    # Check if the file is an HTML file
    if filename.endswith('.html'):
        # Construct the full path to the HTML file
        html_path = os.path.join(html_dir, filename)

        # Read the HTML file
        with open(html_path, 'r') as html_file:
            html_content = html_file.read()

        # Convert the HTML to Markdown
        markdown_content = html2text.html2text(html_content)

        # Construct the full path to the Markdown file
        markdown_path = os.path.join(markdown_dir, filename[:-5] + '.md')

        # Write the Markdown file
        with open(markdown_path, 'w') as markdown_file:
            markdown_file.write(markdown_content)
