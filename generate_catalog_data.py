import os
import re

categories_config = [
    {
        "id": "awards",
        "name": "Awards & Wooden Trophies",
        "tagline": "Honor extraordinary achievements with timeless artisan wooden trophies and plaques"
    },
    {
        "id": "heritage",
        "name": "Heritage & Commemorative Frames",
        "tagline": "Marking history, milestones, and prestigious corporate achievements"
    },
    {
        "id": "desk",
        "name": "Desk & Office Accessories",
        "tagline": "Elevate the executive workspace with artisanal utility and craftsmanship"
    },
    {
        "id": "showpieces",
        "name": "Table Showpieces & Wall Mounts",
        "tagline": "Artisan tabletop illumination, cabin signage & everyday lifestyle utilities"
    }
]

products = [
    # AWARDS & WOODEN TROPHIES (1-8)
    {
        "id": 1,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "Wood trophy 1.jpeg",
        "name": "Five-Star Royal Shield Wooden Trophy",
        "desc": "Layered natural birch and dark walnut shield memento with five-star honor badge and precision laser-engraved citation text on a stable standing easel base."
    },
    {
        "id": 2,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "wood trophy 2.jpeg",
        "name": "Classic Wooden Goblet Trophy Award",
        "desc": "Dual-tone laser-crafted birch and dark walnut goblet cup memento engineered for academic, institutional, and corporate excellence recognitions."
    },
    {
        "id": 3,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "wood trophy 3.jpeg",
        "name": "Geometric Diamond Shield Wooden Plaque",
        "desc": "Diamond-crested dual-tone wooden award featuring intricate filigree borders, center laser-etched dedication plate, and modern geometric silhouette."
    },
    {
        "id": 4,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "wood trophy 4.jpeg",
        "name": "Educator's Easel Desktop Plaque",
        "desc": "Multi-layered 3D wooden desk plaque depicting a classic book stack, spectacles, and pencil caddy with customizable laser-engraved citation area."
    },
    {
        "id": 5,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "wood trophy 5.jpeg",
        "name": "Star Performer Wooden Trophy",
        "desc": "Iconic five-point star award crafted in warm natural wood veneer with dark walnut trim and personalized motivational citation engraving."
    },
    {
        "id": 6,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "wood trophy 6.jpeg",
        "name": "Classroom Blackboard Doodle Wooden Memento",
        "desc": "Artisan wooden easel plaque featuring fine laser-etched stationery, geometry, chemistry, and book illustrations celebrating academic guidance."
    },
    {
        "id": 7,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "wood trophy special.jpeg",
        "name": "Prestige Citation of Recognition Wooden Plaque",
        "desc": "Handcrafted dark walnut beveled citation plaque mounted with an ornate laser-etched brushed gold filigree brass faceplate for landmark corporate honors."
    },
    {
        "id": 8,
        "cat": "awards",
        "cat_name": "Awards & Wooden Trophies",
        "file": "plaque trophy.jpeg",
        "name": "Asia Book of Records Gold Certificate Plaque",
        "desc": "High-gloss deep mahogany finish citation plaque with ornate gold filigree metal certificate plate designed for prestigious national and global records."
    },

    # HERITAGE FRAMES & COMMEMORATIVE DISPLAYS (9-16)
    {
        "id": 9,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame1.jpeg",
        "name": "Indian Navy Retirement Commemorative Silver Salver Frame",
        "desc": "Die-struck royal silver salver with gold naval emblem mounted on deep royal navy velvet backing inside a refined brushed silver metallic frame."
    },
    {
        "id": 10,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame2.jpeg",
        "name": "Doctor's Advanced Fellowship Certificate Display Frame",
        "desc": "Executive credential display frame with gold inner fillet, dual-seal mount, and anti-reflective glass for medical, academic, and fellowship honors."
    },
    {
        "id": 11,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame3.jpeg",
        "name": "INS Vikrant R11 Ironhearts & Crest Dual Medallion Frame",
        "desc": "Natural oak wood shadowbox housing dual commemorative enamel medallions honoring naval engineering legacy and distinguished service."
    },
    {
        "id": 12,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame4.jpeg",
        "name": "Royal Gold Scalloped Filigree Salver Plaque Frame",
        "desc": "Scalloped gold honor salver plate with portrait vignette mounted on textured burgundy leatherette in a luxury beveled gold-trimmed frame."
    },
    {
        "id": 13,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame5.jpeg",
        "name": "Edelweiss Tokio Gold Assessor Medal & Certificate Shadowbox",
        "desc": "Dual-window deep shadowbox frame presenting an embossed gold ribbon medal alongside the official corporate citation parchment with gold bevels."
    },
    {
        "id": 14,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame6.jpeg",
        "name": "ASUS Intel Pinnacle Partner Award Floating Glass Frame",
        "desc": "Contemporary minimalist floating glass partner award frame featuring metallic gold typography on a suspended matte onyx centerpiece."
    },
    {
        "id": 15,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame7.jpeg",
        "name": "Drawing Olympiad Certificate of Appreciation Plaque",
        "desc": "Radiant gold-rimmed desktop acrylic plaque featuring refined botanical gold motifs on royal sapphire acrylic for educator and student milestones."
    },
    {
        "id": 16,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative Frames",
        "file": "Frame8.jpeg",
        "name": "JioStar Project Crest Leadership Citation Plaque",
        "desc": "Executive gold-beveled citation plaque featuring personalized leadership commendation on a midnight black textured acrylic finish."
    },

    # DESK & OFFICE ACCESSORIES (17-23)
    {
        "id": 17,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "Desk organizer.jpeg",
        "name": "Minimalist Illuminated Wooden Desk Cabinet Organizer",
        "desc": "Dovetail-joint natural oak cabinet organizer featuring a transparent sliding acrylic door, dedicated phone stand, stationery shelves, and warm ambient LED lighting."
    },
    {
        "id": 18,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "Desk organizer2.jpeg",
        "name": "Natural Solid Beechwood Beverage Coaster Set",
        "desc": "Set of 6 square solid beechwood drink coasters with precision laser-engraved corporate branding, nestled inside a matching handcrafted open-slot wooden caddy."
    },
    {
        "id": 19,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "Desk organizer3.jpeg",
        "name": "Royal Enfield Ridecraft Custom Desk Photo Frame",
        "desc": "Automotive-themed desktop picture frame featuring bold racing pinstripes and a customized 3D motorcycle metal brand badge."
    },
    {
        "id": 20,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "Desk organizer4.jpeg",
        "name": "Baby Groot Character Pen Holder & Memento",
        "desc": "Artisan layered wood Groot figurine organizer with integrated solid wood pen barrel and personalized collegiate desktop plaque."
    },
    {
        "id": 21,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "desk organiser 5.jpeg",
        "name": "Canine Crest Matte Black Silhouette Phone Dock & Stand",
        "desc": "Precision laser-cut matte black dog silhouette phone stand with an elevated circular pedestal base and integrated cable routing slot."
    },
    {
        "id": 22,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "desk organiser 6.jpeg",
        "name": "Illuminated ADCET Alumni LED Acrylic Memento & Pen Stand",
        "desc": "Backlit warm LED crystal acrylic crest trophy with integrated executive desk pen holder on a rich matte black illuminated base."
    },
    {
        "id": 23,
        "cat": "desk",
        "cat_name": "Desk & Office Accessories",
        "file": "Desk organiser6.jpeg",
        "name": "Executive Wooden Desk Clock, Calendar & Pen Caddy",
        "desc": "Handcrafted beechwood desk centerpiece featuring a gold quartz analog clock, perpetual calendar blocks, business card dock, and wooden executive pen."
    },

    # TABLE SHOWPIECES, WALL MOUNTS & LIFESTYLE (24-29)
    {
        "id": 24,
        "cat": "showpieces",
        "cat_name": "Table Showpieces & Wall Mounts",
        "file": "tavble showpiece 1.jpeg",
        "name": "Havells Divine Lord Ganesha LED Acrylic Table Showpiece",
        "desc": "Lord Ganesha precision laser-etched warm LED acrylic award mounted on a customized corporate branded matte pedestal with 'Energy to Rule Your Kingdom' slogan."
    },
    {
        "id": 25,
        "cat": "showpieces",
        "cat_name": "Table Showpieces & Wall Mounts",
        "file": "tavble showpiece 2.jpeg",
        "name": "Sacred Om / Ik Onkar Spiritual Motif Illuminated LED Lamp",
        "desc": "Laser-etched sacred spiritual motif acrylic plate illuminated by warm edge lighting on a sleek matte black pedestal base for desks and sacred spaces."
    },
    {
        "id": 26,
        "cat": "showpieces",
        "cat_name": "Table Showpieces & Wall Mounts",
        "file": "Wall holding 1.jpeg",
        "name": "Custom Clinic Sliding 'Doctor In / Doctor Out' Door Sign",
        "desc": "Branded acrylic sliding nameplate with bold status indicators and pharmaceutical sponsorship branding for private consultation cabins and executive suites."
    },
    {
        "id": 27,
        "cat": "showpieces",
        "cat_name": "Table Showpieces & Wall Mounts",
        "file": "wall holding 2.jpeg",
        "name": "Custom Polaroid Magnetic Photo Frames (Set of 3)",
        "desc": "Colorful brandable magnetic photo frames for refrigerators, lockers, and metal workstation partitions with quick-slide top photo insert slots."
    },
    {
        "id": 28,
        "cat": "showpieces",
        "cat_name": "Table Showpieces & Wall Mounts",
        "file": "Wall holding 3.jpeg",
        "name": "SugaSure FutureLife Magnetic Message & Photo Frame",
        "desc": "Sleek black and gold magnetic photo and message frame with corporate branding ('Hold close, The moments That matter.') for clinic and desk panels."
    },
    {
        "id": 29,
        "cat": "showpieces",
        "cat_name": "Table Showpieces & Wall Mounts",
        "file": "WhatsApp Image 2026-06-07 at 5.40.14 PM.jpeg",
        "name": "Executive Travel Toiletry & Grooming Kit Dopp Pouch",
        "desc": "Water-resistant teal ballistic nylon dopp kit with structured dual-zip opening, reinforced top grab handle, and custom metal zipper puller."
    }
]

def generate_catalog_html():
    lines = []
    
    # Category Tabs
    lines.append('<div class="category-tabs" id="categoryTabs" role="tablist" aria-label="Product categories">')
    lines.append('  <button class="tab-btn active" role="tab" data-category="all" id="tab-all" aria-selected="true" aria-controls="catalog-grid">All</button>')
    for cat in categories_config:
        lines.append(f'  <button class="tab-btn" role="tab" data-category="{cat["id"]}" id="tab-{cat["id"]}" aria-selected="false">{cat["name"]}</button>')
    lines.append('</div>')
    lines.append('')
    lines.append('<div class="product-grid" id="catalog-grid" role="tabpanel">')
    
    for cat in categories_config:
        cat_products = [p for p in products if p['cat'] == cat['id']]
        if not cat_products:
            continue
        
        lines.append(f'  <div class="category-block" data-category="{cat["id"]}">')
        lines.append('    <div class="category-title-bar">')
        lines.append(f'      <h3 class="category-name">{cat["name"]}</h3>')
        lines.append(f'      <span class="category-tagline">{cat["tagline"]}</span>')
        lines.append('    </div>')
        lines.append('    <div class="products-row">')
        
        for p in cat_products:
            img_src = f'catlogue/catlogue/{p["file"]}'
            lines.append(f'      <article class="product-card" id="product-{p["id"]}" data-animate="card">')
            lines.append('        <div class="product-image-zone">')
            lines.append(f'          <img src="{img_src}" alt="{p["name"]}" class="product-photo" loading="lazy" />')
            lines.append(f'          <div class="product-num">S — {p["id"]:02d}</div>')
            lines.append('        </div>')
            lines.append('        <div class="product-card-body">')
            lines.append(f'          <span class="product-category-tag">{p["cat_name"]}</span>')
            lines.append(f'          <h4 class="product-name">{p["name"]}</h4>')
            lines.append(f'          <p class="product-desc">{p["desc"]}</p>')
            lines.append('        </div>')
            lines.append('      </article>')
                
        lines.append('    </div>')
        lines.append('  </div>')
        lines.append('')
        
    lines.append('</div>')
    return '\n'.join(lines)

if __name__ == '__main__':
    catalog_markup = generate_catalog_html()
    with open(r'e:\cat\generated_catalog.html', 'w', encoding='utf-8') as f:
        f.write(catalog_markup)
    print(f'Successfully generated catalog HTML with {len(products)} products.')
