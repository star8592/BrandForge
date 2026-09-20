import json
from pathlib import Path


def build_report(items, output='brand_report.html'):
    rows = ''.join(
        f'<tr><td>{x.get("name", "")}</td><td>{x.get("score", 0)}</td></tr>'
        for x in items
    )

    html = f'''<!doctype html>
<html>
<head><title>BrandForge Report</title></head>
<body>
<h1>BrandForge Ranking</h1>
<table border="1">
<tr><th>Name</th><th>Score</th></tr>
{rows}
</table>
</body>
</html>'''

    Path(output).write_text(html, encoding='utf-8')


if __name__ == '__main__':
    build_report([])
