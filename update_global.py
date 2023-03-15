# After editing the global blocks just run: python3 update_global.py
import os, re, sys

# The names of the blocks of code to be added to each html file
blocks = {'menu', 'style', 'comments', 'mathjax'}
pattern = {}
content = {}


# Define regular expression pattern to match for finding and replacing the html blocks, and load content
for block in blocks:
  pattern[block] =  r'<!--begin '+block+'-->[\s\S]*?<!--end '+block+'-->'
  block_file = open('global/html/'+block+'.html', 'r') 
  content[block] = '<!--begin '+block+'-->'+block_file.read()+'<!--end '+block+'-->'
  block_file.close()


# Loop through all HTML files in the current directory
for filename in os.listdir():
  if filename.endswith('.html'):
      # Open the file for reading
      with open(filename, 'r') as page_file:
          # Read the file contents
          file_content = page_file.read()
          for block in blocks:
            # Update the blocks in the file content
            file_content = re.sub(pattern[block], content[block], file_content)
            if block == 'comments':
              # Add unique identifier for the comments 
              file_content = re.sub('FILE_NAME', filename[:len(filename)-5], file_content)
          # Remove any extra vertical whitespace at the end of the file
          file_content=re.sub(r"^\s+", "", file_content, flags = re.MULTILINE)
          file_content += "\n"
      # Open the file for writing and overwrite the old contents
      with open(filename, 'w') as f:
          f.write(file_content)
