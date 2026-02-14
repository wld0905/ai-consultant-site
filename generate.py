import markdown

# Read markdown content
with open("content.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert to HTML
html_body = markdown.markdown(md_content)

# Basic HTML template
html_page = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AI Consultant – Waly Diouf</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: auto;
            padding: 40px;
            background: #f4f4f4;
        }}
        h1, h2 {{
            color: #222;
        }}
        a {{
            color: blue;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

# Write to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("Site generated: index.html")
