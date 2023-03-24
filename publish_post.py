#FIRST MOVE HTML FILE FROM DRAFTS TO MAIN HTML FOLDER, THEN RUN THIS SCRIPT
#usage: python3 publish_post.py [html/post]

import os, re, sys
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%m/%d/%Y")

post_file_name = sys.argv[1]
tags = ''
for i in range(2, len(sys.argv)):
  tags += sys.argv[i]+', '
tags = tags[:-2]

new_post_file = open(post_file_name, 'r')
new_post_content = new_post_file.read()
new_post_title = re.findall(r"<h1>(.*?)</h1>", new_post_content)[0]
new_post_file.close()

posts_file = open('html/posts.html', 'r+')
posts_content = posts_file.read()
posts_content = re.sub('<!--new post-->', '<!--new post-->\n<li>'+date_time \
  +' - <a href="../'+post_file_name+'">'+new_post_title+'</a> - '+tags+'</li>', posts_content)

posts_file.seek(0)
posts_file.write(posts_content)
posts_file.close()

