with open(r"e:\cat\index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

with open(r"e:\cat\generated_catalog.html", "r", encoding="utf-8") as f:
    new_catalog = f.read()

start_marker = '<div class="category-tabs" id="categoryTabs"'
end_marker = '      </div>\n    </section>\n\n    <!-- ═══════════════════════════════════════════\n         SECTION 4 — BESPOKE CUSTOMIZATION'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Indent new catalog nicely if desired, or insert as is
    indented_catalog = "\n".join("        " + line if line else "" for line in new_catalog.split("\n"))
    new_html = html_content[:start_idx] + indented_catalog + "\n" + html_content[end_idx:]
    with open(r"e:\cat\index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Successfully replaced catalog section in index.html.")
else:
    print("Could not find markers.", start_idx, end_idx)
