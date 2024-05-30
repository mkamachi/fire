import sys
from jinja2 import Template

issue_title = sys.argv[1]
issue_body = sys.argv[2]
issue_number = sys.argv[3]

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Issue {{ number }}: {{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        p { font-size: 1.2em; }
        .issue-body { white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>Issue #{{ number }}: {{ title }}</h1>
    <div class="issue-body">{{ body }}</div>
</body>
</html>
"""

template = Template(html_template)
html_content = template.render(title=issue_title, body=issue_body, number=issue_number)

file_name = f"issue_{issue_number}.html"
with open(file_name, 'w') as f:
    f.write(html_content)

