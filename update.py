import os

files = [r'e:\cat\index.html', r'e:\cat\generated_catalog.html', r'e:\cat\app.js', r'e:\cat\style.css']

for file_path in files:
    if not os.path.exists(file_path):
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace company names
    content = content.replace('Prestige &amp; Co.', 'Minal Industres')
    content = content.replace('Prestige <span class="amp">&</span> Co.', 'Minal Industres')
    content = content.replace('Prestige & Co.', 'Minal Industres')
    content = content.replace('Prestige', 'Minal')
    content = content.replace('PRESTIGE & CO.', 'MINAL INDUSTRES')
    content = content.replace('PRESTIGE', 'MINAL')

    # Replace website and email
    content = content.replace('prestige-co.com', 'minal-industres.com')

    if 'index.html' in file_path:
        # Replace phone numbers
        content = content.replace('+1 (800) 774-3384', '+91 9137773967')
        content = content.replace('tel:+18007743384', 'tel:+919137773967')

        # Add whatsapp link
        old_phone_html = '<a href="tel:+919137773967" class="contact-link" id="phoneLink">+91 9137773967</a>'
        new_phone_html = old_phone_html + '\n                  <a href="https://wa.me/919137773967" class="contact-link" id="whatsappLink" target="_blank">Connect on WhatsApp</a>'
        content = content.replace(old_phone_html, new_phone_html)

        # Update cover footer
        cover_footer_target = '<div class="cover-footer-bar">\n        <span>minal-industres.com</span>\n        <span>gifts@minal-industres.com</span>\n        <span>+91 9137773967</span>\n      </div>'
        cover_footer_replacement = '<div class="cover-footer-bar">\n        <span>minal-industres.com</span>\n        <span>gifts@minal-industres.com</span>\n        <span>+91 9137773967</span>\n        <span><a href="https://wa.me/919137773967" style="color: inherit; text-decoration: underline;">WhatsApp Us</a></span>\n      </div>'
        content = content.replace(cover_footer_target, cover_footer_replacement)

        # Replace Catalog No
        content = content.replace('PCG-2026', 'MI-2026')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated files successfully')
