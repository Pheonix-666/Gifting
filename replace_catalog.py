import re

with open(r"e:\cat\index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

with open(r"e:\cat\generated_catalog.html", "r", encoding="utf-8") as f:
    new_catalog = f.read()

start_marker = '<div class="category-tabs" id="categoryTabs"'
end_marker = '    <!-- ═══════════════════════════════════════════\n         SECTION 4 — BESPOKE CUSTOMIZATION'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Append the end marker back since we split before it
    new_html = html_content[:start_idx] + new_catalog + "\n\n" + html_content[end_idx:]
    with open(r"e:\cat\index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Successfully replaced catalog section.")
else:
    print("Could not find markers.", start_idx, end_idx)
