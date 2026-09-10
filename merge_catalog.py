with open(r'e:\cat\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open(r'e:\cat\generated_catalog.html', 'r', encoding='utf-8') as f:
    catalog = f.read()

start_marker = '<div class="category-tabs"'
end_marker = '<!-- ═══════════════════════════════════════════\n         SECTION 4 — BESPOKE CUSTOMIZATION'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

print(f"start_idx: {start_idx}, end_idx: {end_idx}")

if start_idx != -1 and end_idx != -1:
    # Notice the section closes before section 4
    # let's find the closing </section> of #catalog
    catalog_close_idx = html.rfind('</section>', start_idx, end_idx)
    new_html = html[:start_idx] + catalog + '\n      </div>\n    </section>\n\n    ' + html[end_marker_pos:] if 'end_marker_pos' in locals() else html[:start_idx] + catalog + '\n      </div>\n    </section>\n\n    ' + html[end_idx:]
    with open(r'e:\cat\index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated index.html!")
