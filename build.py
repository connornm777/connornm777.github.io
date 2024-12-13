import os
from pathlib import Path
import markdown
import yaml
from collections import defaultdict
import re  # For regex operations
from bs4 import BeautifulSoup  # For HTML prettification

# Directories
SRC_DIR = Path("src")
OUTPUT_DIR = Path("html")
TEMPLATE_ARTICLE = Path("templates/article.html")
TEMPLATE_HOMEPAGE = Path("templates/homepage.html")

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# Load the templates
with TEMPLATE_ARTICLE.open("r", encoding="utf-8") as f:
    article_template = f.read()

with TEMPLATE_HOMEPAGE.open("r", encoding="utf-8") as f:
    homepage_template = f.read()

# Function to prettify HTML with tab indents
def prettify_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    pretty = soup.prettify()
    # Replace 4 spaces with a tab in each line
    pretty_with_tabs = '\n'.join(line.replace('    ', '\t') for line in pretty.split('\n'))
    return pretty_with_tabs

# Function to extract math expressions and replace them with placeholders
def extract_math(content):
    """
    Extracts all math expressions from the content and replaces them with placeholders.

    Returns:
        modified_content: Content with math expressions replaced by placeholders.
        math_expressions: List of extracted math expressions.
    """
    math_expressions = []

    # Patterns to match display and inline math
    # Display math: $$...$$
    # Inline math: $...$ but not $$...$$
    display_math_pattern = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)
    inline_math_pattern = re.compile(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$', re.DOTALL)

    # Replace display math first
    def replace_display(match):
        math = match.group(0)  # Includes $$ delimiters
        placeholder = f"BOOGERMATHEXPR{len(math_expressions)}BOOGER"
        math_expressions.append(math)
        return placeholder

    content = display_math_pattern.sub(replace_display, content)

    # Then replace inline math
    def replace_inline(match):
        math = match.group(0)  # Includes $ delimiters
        placeholder = f"BOOGERMATHEXPR{len(math_expressions)}BOOGER"
        math_expressions.append(math)
        return placeholder

    content = inline_math_pattern.sub(replace_inline, content)

    return content, math_expressions

# Function to restore math expressions from placeholders
def restore_math(content, math_expressions):
    """
    Restores math expressions in the content by replacing placeholders with original math.

    Args:
        content: HTML content with placeholders.
        math_expressions: List of original math expressions.

    Returns:
        Content with math expressions restored.
    """
    for idx, math in enumerate(math_expressions):
        placeholder = f"BOOGERMATHEXPR{idx}BOOGER"
        # Use a lambda to return the math string without interpreting backslashes
        content = re.sub(re.escape(placeholder), lambda match: math, content)
    return content

# Parse Markdown with metadata and protect math expressions
def parse_markdown(md_file):
    with md_file.open("r", encoding="utf-8") as f:
        content = f.read()

    # Split front matter from body
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            body = parts[2]
            metadata = yaml.safe_load(front_matter)
        else:
            metadata = {}
            body = content
    else:
        metadata = {}
        body = content

    # Extract math expressions
    body_modified, math_expressions = extract_math(body)

    # Convert Markdown to HTML with 'attr_list' extension
    html_content = markdown.markdown(body_modified, extensions=['markdown.extensions.attr_list'])

    # Restore math expressions in HTML
    html_content = restore_math(html_content, math_expressions)

    return metadata, html_content

# Collect all Markdown files and metadata
posts = []
tags = defaultdict(list)  # To organize posts by tags

for md_file in SRC_DIR.glob("*.md"):
    metadata, html_content = parse_markdown(md_file)
    metadata["content"] = html_content
    metadata["slug"] = f"{md_file.stem}.html"
    metadata["tags"] = metadata.get("tags", [])
    metadata["title"] = metadata.get("title", md_file.stem)
    posts.append(metadata)

    # Organize posts by tags
    for tag in metadata["tags"]:
        tags[tag].append(metadata)

# Function to generate tag menus with links
def generate_tag_menus(tags_dict, posts_list):
    tag_menus = "\n".join(
        f'<div class="tag-menu"><h2>{tag.title()}</h2><ul>' +
        "".join(
            f'<li><a href="{post["slug"]}">{post["title"]}</a></li>'
            for post in sorted(posts_list, key=lambda x: x["slug"])
        ) +
        "</ul></div>"
        for tag, posts_list in tags_dict.items()
    )
    return f"<div class='tag-container'>{tag_menus}</div>"

# Generate HTML for each post
for post in posts:
    output_file = OUTPUT_DIR / post["slug"]

    # Generate tag links
    tag_links = " | ".join(tag.title() for tag in post["tags"])
    header_links = f'<a href="home.html">Homepage</a> | {tag_links}' if tag_links else '<a href="home.html">Homepage</a>'

    # Populate the article template
    page_content = article_template.replace("<!--header-->", header_links)
    page_content = page_content.replace("<!--content-->", post["content"])

    # Disqus variables (ensure 'example' is replaced correctly)
    page_content = page_content.replace("example.html", post["slug"])
    page_content = page_content.replace("example", post["slug"].replace(".html", ""))

    # Prettify HTML with tabs
    page_content_pretty = prettify_html(page_content)

    # Write the output file with tab-indented HTML
    with output_file.open("w", encoding="utf-8") as f:
        f.write(page_content_pretty)

# Generate the homepage grouped by tags
tag_menus_html = generate_tag_menus(tags, posts)
homepage_content = homepage_template.replace("<!--menu-->", tag_menus_html)

# Prettify homepage HTML with tabs
homepage_content_pretty = prettify_html(homepage_content)

with (OUTPUT_DIR / "home.html").open("w", encoding="utf-8") as f:
    f.write(homepage_content_pretty)

print("Site built successfully!")
