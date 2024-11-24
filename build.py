import os
from pathlib import Path
import markdown
import yaml
from datetime import datetime

# Directories
SRC_DIR = Path("src")
OUTPUT_DIR = Path("website/html")
TEMPLATE_FILE = Path("templates/example.html")

OUTPUT_DIR.mkdir(exist_ok=True)

# Load the HTML template
with TEMPLATE_FILE.open("r", encoding="utf-8") as f:
    template = f.read()

# Parse Markdown with metadata
def parse_markdown(md_file):
    with md_file.open("r", encoding="utf-8") as f:
        content = f.read()
    # Split front matter from body
    if content.startswith("---"):
        front_matter, body = content.split("---", 2)[1:]
        metadata = yaml.safe_load(front_matter)
        html_content = markdown.markdown(body)
        return metadata, html_content
    return {}, markdown.markdown(content)

# Collect all Markdown files and metadata
posts = []
for md_file in SRC_DIR.glob("*.md"):
    metadata, html_content = parse_markdown(md_file)
    metadata["content"] = html_content
    metadata["slug"] = f"{md_file.stem}.html"
    metadata["date"] = datetime.strptime(metadata["date"], "%Y-%m-%d")
    posts.append(metadata)

# Sort posts by date
posts.sort(key=lambda x: x["date"], reverse=True)

# Generate dynamic menu
menu_items = "\n".join(
    f'<li><a href="{post["slug"]}">{post["title"]}</a></li>' for post in posts
)

# Generate HTML pages
for post in posts:
    output_file = OUTPUT_DIR / post["slug"]
    
    # Populate the template
    page_content = template.replace("<!--menu-->", f"<ul>{menu_items}</ul>")
    page_content = page_content.replace("<!--content-->", post["content"])
    
    # Disqus variables
    page_content = page_content.replace("example.html", post["slug"])
    page_content = page_content.replace("example", post["slug"].replace(".html", ""))
    
    with output_file.open("w", encoding="utf-8") as f:
        f.write(page_content)


print("Site built successfully!")
