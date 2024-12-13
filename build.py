import os
from pathlib import Path
import markdown
import yaml
from collections import defaultdict

# Directories
SRC_DIR = Path("src")
OUTPUT_DIR = Path("html")
TEMPLATE_ARTICLE = Path("templates/article.html")
TEMPLATE_HOMEPAGE = Path("templates/homepage.html")

OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

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
        # Enable 'attr_list' extension using the full path
        html_content = markdown.markdown(body, extensions=['markdown.extensions.attr_list'])
        return metadata, html_content
    return {}, markdown.markdown(content, extensions=['markdown.extensions.attr_list'])


# Collect all Markdown files and metadata
posts = []
tags = defaultdict(list)  # To organize posts by tags

for md_file in SRC_DIR.glob("*.md"):
    metadata, html_content = parse_markdown(md_file)
    metadata["content"] = html_content
    metadata["slug"] = f"{md_file.stem}.html"
    metadata["tags"] = metadata.get("tags", [])
    posts.append(metadata)

    # Organize posts by tags
    for tag in metadata["tags"]:
        tags[tag].append(metadata)

# Generate HTML for each post
for post in posts:
    output_file = OUTPUT_DIR / post["slug"]

    # Generate tag links
    tag_links = " | ".join(tag.title() for tag in post["tags"])
    header_links = f'<a href="home.html">Homepage</a> | {tag_links}'

    # Populate the article template
    page_content = article_template.replace("<!--header-->", header_links)
    page_content = page_content.replace("<!--content-->", post["content"])

    # Disqus variables
    page_content = page_content.replace("example.html", post["slug"])
    page_content = page_content.replace("example", post["slug"].replace(".html", ""))

    # Write the output file
    with output_file.open("w", encoding="utf-8") as f:
        f.write(page_content)

# Generate the homepage grouped by tags
tag_menus = "\n".join(
    f'<div class="tag-menu"><h2>{tag.title()}</h2><ul>' +
    "".join(
        f'<li><a href="{post["slug"]}">{post["title"]}</a></li>'
        for post in sorted(posts, key=lambda x: x["slug"])
    ) +
    "</ul></div>"
    for tag, posts in tags.items()
)

homepage_content = homepage_template.replace("<!--menu-->", f"<div class='tag-container'>{tag_menus}</div>")

with (OUTPUT_DIR / "home.html").open("w", encoding="utf-8") as f:
    f.write(homepage_content)

print("Site built successfully!")
