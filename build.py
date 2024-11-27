import os
from pathlib import Path
import markdown
import yaml
from datetime import datetime

# Directories
SRC_DIR = Path("src")
OUTPUT_DIR = Path("website/html")
TEMPLATE_ARTICLE = Path("templates/article.html")
TEMPLATE_HOMEPAGE = Path("templates/homepage.html")

OUTPUT_DIR.mkdir(exist_ok=True)

# Load the templates
with TEMPLATE_ARTICLE.open("r", encoding="utf-8") as f:
    article_template = f.read()

with TEMPLATE_HOMEPAGE.open("r", encoding="utf-8") as f:
    homepage_template = f.read()

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

# Generate HTML for each post
for i, post in enumerate(posts):
    output_file = OUTPUT_DIR / post["slug"]

    # Determine navigation
    prev_link = (
        f'<a href="{posts[i-1]["slug"]}">&larr; {posts[i-1]["title"]}</a>' if i > 0 else ""
    )
    next_link = (
        f'<a href="{posts[i+1]["slug"]}">{posts[i+1]["title"]} &rarr;</a>'
        if i < len(posts) - 1
        else ""
    )
    nav_links = f"{prev_link} | <a href='home.html'>Back to Homepage</a> | {next_link}"

    # Populate the article template
    page_content = article_template.replace("<!--menu-->", nav_links)
    page_content = page_content.replace("<!--content-->", post["content"])

    # Disqus variables
    page_content = page_content.replace("example.html", post["slug"])
    page_content = page_content.replace("example", post["slug"].replace(".html", ""))

    with output_file.open("w", encoding="utf-8") as f:
        f.write(page_content)

# Generate the homepage
homepage_links = "\n".join(
    f'<li><a href="{post["slug"]}">{post["title"]}</a> - {post["date"].strftime("%Y-%m-%d")}</li>'
    for post in posts
)
homepage_content = homepage_template.replace("<!--menu-->", f"<ul>{homepage_links}</ul>")

with (OUTPUT_DIR / "home.html").open("w", encoding="utf-8") as f:
    f.write(homepage_content)

print("Site built successfully!")
