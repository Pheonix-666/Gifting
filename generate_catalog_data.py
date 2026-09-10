import os
import re

# Comprehensive, accurate list of all 41 products
categories_config = [
    {
        "id": "awards",
        "name": "Awards & Recognition",
        "tagline": "Honor the extraordinary with timeless mementos"
    },
    {
        "id": "heritage",
        "name": "Heritage & Commemorative",
        "tagline": "Marking history with premium displays"
    },
    {
        "id": "everyday",
        "name": "Everyday Utilities",
        "tagline": "Premium gifts for the journey and the routine"
    },
    {
        "id": "desk",
        "name": "Desk & Office",
        "tagline": "Elevate the workspace"
    },
    {
        "id": "custom",
        "name": "Bespoke & Customized Products",
        "tagline": "Tailor-made specifically for your brand"
    },
    {
        "id": "new",
        "name": "Latest Additions",
        "tagline": "Freshly curated, just arrived in our collection"
    }
]

products = [
    # AWARDS & RECOGNITION (1-9)
    {
        "id": 1,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.43 AM.jpeg",
        "name": "Illuminated LED Acrylic Alumni Memento & Pen Stand",
        "desc": "Backlit warm LED crystal acrylic crest trophy with integrated luxury desk pen holder on a rich matte black base.",
        "type": "image"
    },
    {
        "id": 2,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.44 AM (1).jpeg",
        "name": "Havells Divine LED Acrylic Trophy",
        "desc": "Lord Ganesha precision laser-etched warm LED acrylic award mounted on a customized corporate branded matte pedestal.",
        "type": "image"
    },
    {
        "id": 3,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.44 AM.jpeg",
        "name": "Classic Wooden Goblet Trophy TD-4 (5\"x6\")",
        "desc": "Dual-tone laser-crafted birch and dark walnut goblet memento designed for academic and corporate excellence honors.",
        "type": "image"
    },
    {
        "id": 4,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.45 AM (1).jpeg",
        "name": "Geometric Shield Wooden Plaque TD-5 (5\"x6\")",
        "desc": "Diamond-crested dual-tone wooden memento featuring intricate filigree borders and custom laser-engraved citation text.",
        "type": "image"
    },
    {
        "id": 5,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.45 AM (2).jpeg",
        "name": "Classroom Blackboard Memento TD-11 (5\"x6\")",
        "desc": "Playfully illustrated wooden memento featuring fine laser-etched stationery and geometry motifs with standing easel base.",
        "type": "image"
    },
    {
        "id": 6,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.45 AM.jpeg",
        "name": "Star Performer Wooden Trophy TD-7 (5\"x6\")",
        "desc": "Iconic five-point wooden star award with dark walnut trim and personalized laser-etched motivational citation.",
        "type": "image"
    },
    {
        "id": 7,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.46 AM (1).jpeg",
        "name": "Five-Star Royal Crest Trophy TD-3 (5\"x6\")",
        "desc": "Sovereign heraldic shield trophy in layered natural wood veneers with five-star honor badge and custom engraving.",
        "type": "image"
    },
    {
        "id": 8,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.46 AM.jpeg",
        "name": "Educator's Easel Desktop Plaque TD-10 (5\"x6\")",
        "desc": "Layered 3D wooden desk plaque depicting classic book stack, glasses, and pencil holder with custom message plate.",
        "type": "image"
    },
    {
        "id": 9,
        "cat": "awards",
        "cat_name": "Awards & Recognition",
        "file": "WhatsApp Image 2026-05-28 at 10.11.47 AM.jpeg",
        "name": "Asia Book of Records Gold Certificate Plaque",
        "desc": "High-gloss deep mahogany finish citation plaque with ornate gold filigree metal certificate plate for landmark records.",
        "type": "image"
    },

    # HERITAGE & COMMEMORATIVE (10-20)
    {
        "id": 10,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.25 AM (1).jpeg",
        "name": "Indian Navy Retirement Commemorative Silver Salver Frame",
        "desc": "Die-struck royal silver salver with gold navy emblem mounted on deep velvet backing in a brushed silver frame.",
        "type": "image"
    },
    {
        "id": 11,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.25 AM (2).jpeg",
        "name": "Executive Fellowship Certificate Display Frame",
        "desc": "Academic and medical credential display frame with gold inner fillet, anti-reflective glazing, and dual-seal mount.",
        "type": "image"
    },
    {
        "id": 12,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.25 AM.jpeg",
        "name": "INS Vikrant Ironhearts & Crest Dual Medallion Frame",
        "desc": "Natural oak wood shadowbox housing dual commemorative enamel medallions honoring naval engineering heritage.",
        "type": "image"
    },
    {
        "id": 13,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.26 AM (1).jpeg",
        "name": "Royal Gold Filigree Salver Frame Plaque",
        "desc": "Scalloped gold honor plate with photo vignette mounted on textured burgundy leatherette in a bright gold frame.",
        "type": "image"
    },
    {
        "id": 14,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.26 AM (2).jpeg",
        "name": "Edelweiss Gold Assessor Medal & Certificate Shadowbox",
        "desc": "Dual-window shadowbox frame presenting an embossed gold ribbon medal alongside the official citation parchment.",
        "type": "image"
    },
    {
        "id": 15,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.26 AM.jpeg",
        "name": "ASUS Intel Pinnacle Partner Floating Glass Frame",
        "desc": "Minimalist floating glass partner award frame with metallic gold typography on matte onyx centerpiece.",
        "type": "image"
    },
    {
        "id": 16,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.27 AM (1).jpeg",
        "name": "ITPL Sales Excellence Certificate Plaque Pair",
        "desc": "Dual standing high-gloss wood plaques featuring crisp navy-and-gold borders and executive leadership signatures.",
        "type": "image"
    },
    {
        "id": 17,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.27 AM (2).jpeg",
        "name": "Golden Horizon Certificate of Appreciation Plaque",
        "desc": "Radiant gold-framed desktop plaque with botanical gold motifs on royal sapphire acrylic for milestone honors.",
        "type": "image"
    },
    {
        "id": 18,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.27 AM.jpeg",
        "name": "TravClan Legacy Circle Tiered Award Suite",
        "desc": "Trio of contemporary partner recognition desktop plaques featuring gold and silver member medallions.",
        "type": "image"
    },
    {
        "id": 19,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.28 AM (1).jpeg",
        "name": "Olympiad Educator Certificate of Appreciation",
        "desc": "Gold-rimmed standing presentation plaque celebrating excellence and widespread student empowerment.",
        "type": "image"
    },
    {
        "id": 20,
        "cat": "heritage",
        "cat_name": "Heritage & Commemorative",
        "file": "WhatsApp Image 2026-05-28 at 10.13.28 AM.jpeg",
        "name": "JioStar Project Crest Leadership Citation Plaque",
        "desc": "Executive gold-beveled citation plaque featuring personalized leadership commendation on midnight black finish.",
        "type": "image"
    },

    # EVERYDAY UTILITIES (21-30)
    {
        "id": 21,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.11 PM.jpeg",
        "name": "Aura Divine Wooden Jharokha Mandir Shrine",
        "desc": "Gold-plated deity idol enshrined in a handcrafted laser-cut walnut wooden temple frame with backlit filigree.",
        "type": "image"
    },
    {
        "id": 22,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.12 PM (1).jpeg",
        "name": "Executive Wooden Desk Clock, Calendar & Pen Caddy",
        "desc": "Handcrafted beechwood desk centerpiece with gold quartz analog clock, perpetual calendar blocks, and business card dock.",
        "type": "image"
    },
    {
        "id": 23,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.12 PM (2).jpeg",
        "name": "Natural Beechwood Beverage Coaster Set",
        "desc": "Set of 6 square solid beechwood drink coasters nestled inside a matching handcrafted open-slot wooden holder.",
        "type": "image"
    },
    {
        "id": 24,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.12 PM.jpeg",
        "name": "Minimalist Illuminated Wooden Desk Cabinet Organizer",
        "desc": "Dovetail-joint oak organizer with transparent acrylic door, phone stand, stationery shelves, and warm ambient glow.",
        "type": "image"
    },
    {
        "id": 25,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.13 PM (1).jpeg",
        "name": "Long Service Milestone Award Plaque",
        "desc": "Antique bronze laurel wreath relief medallion with gold central plate on a contoured cherry wood base.",
        "type": "image"
    },
    {
        "id": 26,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.13 PM (2).jpeg",
        "name": "Custom Polaroid Magnetic Photo Frames",
        "desc": "Set of colorful brandable magnetic photo frames for refrigerators, lockers, and metal workstation panels.",
        "type": "image"
    },
    {
        "id": 27,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.13 PM.jpeg",
        "name": "Sacred Om Illuminated LED Acrylic Lamp",
        "desc": "Laser-etched spiritual motif acrylic plate illuminated from a sleek matte black LED pedestal for desks and altars.",
        "type": "image"
    },
    {
        "id": 28,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.14 PM.jpeg",
        "name": "Executive Travel Toiletry & Grooming Kit Pouch",
        "desc": "Water-resistant teal ballistic nylon dopp kit with structured zip opening, top grab handle, and custom metal puller.",
        "type": "image"
    },
    {
        "id": 29,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.15 PM.jpeg",
        "name": "Personalized Medical Specialist Ceramic Mug",
        "desc": "Premium high-fired two-tone ceramic mug with personalized professional title and humorous healthcare artwork.",
        "type": "image"
    },
    {
        "id": 30,
        "cat": "everyday",
        "cat_name": "Everyday Utilities",
        "file": "WhatsApp Image 2026-06-07 at 5.40.16 PM.jpeg",
        "name": "Zifi Silver Jubilee Commemorative Medallion Frame",
        "desc": "Silver jubilee medallion mounted with a framed doctor appreciation certificate in an embossed silver border.",
        "type": "image"
    },

    # DESK & OFFICE (31-35)
    {
        "id": 31,
        "cat": "desk",
        "cat_name": "Desk & Office",
        "file": "WhatsApp Image 2026-06-07 at 5.42.45 PM (2).jpeg",
        "name": "Gothic Arch Wooden Pen Holder — Ultimate Collection",
        "desc": "Architectural arched window wooden desk caddy in deep charcoal with birch inlays and custom brand crest plate.",
        "type": "image"
    },
    {
        "id": 32,
        "cat": "desk",
        "cat_name": "Desk & Office",
        "file": "WhatsApp Image 2026-06-07 at 5.42.45 PM.jpeg",
        "name": "Royal Enfield Ridecraft Custom Photo Frame",
        "desc": "Automotive themed desktop picture frame with racing pinstripes and 3D motorcycle metal logo badge.",
        "type": "image"
    },
    {
        "id": 33,
        "cat": "desk",
        "cat_name": "Desk & Office",
        "file": "WhatsApp Image 2026-06-07 at 5.42.46 PM (1).jpeg",
        "name": "Sun Pharma Premium Wooden Presentation Box",
        "desc": "Matte black interlocking finger-joint wooden presentation box featuring gold-foiled corporate emblem.",
        "type": "image"
    },
    {
        "id": 34,
        "cat": "desk",
        "cat_name": "Desk & Office",
        "file": "WhatsApp Image 2026-06-07 at 5.42.46 PM (2).jpeg",
        "name": "Canine Silhouette Desktop Mobile Dock",
        "desc": "Precision laser-cut matte black dog silhouette phone stand with an elevated natural wood pedestal dock.",
        "type": "image"
    },
    {
        "id": 35,
        "cat": "desk",
        "cat_name": "Desk & Office",
        "file": "WhatsApp Image 2026-06-07 at 5.42.46 PM.jpeg",
        "name": "Baby Groot Character Pen Holder & Memento",
        "desc": "Artisan layered wood Groot figurine organizer with pen barrel and institutional collegiate plaque on top.",
        "type": "image"
    },

    # BESPOKE & CUSTOMIZED (36)
    {
        "id": 36,
        "cat": "custom",
        "cat_name": "Bespoke & Customized Products",
        "file": "ChatGPT Image Jun 7, 2026, 05_52_26 PM.png",
        "name": "SugaSure FutureLife Desktop Inspirational Frame",
        "desc": "Corporate branded acrylic desk plaque featuring motivational typography, pharmaceutical branding, and dual-tone mount.",
        "type": "image"
    },

    # LATEST ADDITIONS (37-41)
    {
        "id": 37,
        "cat": "new",
        "cat_name": "Latest Additions",
        "file": "WhatsApp Image 2026-09-10 at 3.25.06 PM.jpeg",
        "name": "Doctor's Day Commemorative Gold-Framed Certificate Plaque",
        "desc": "Textured mahogany patterned frame with gold inner bevel and full-color medical dedication certificate print.",
        "type": "image"
    },
    {
        "id": 38,
        "cat": "new",
        "cat_name": "Latest Additions",
        "file": "WhatsApp Image 2026-09-10 at 3.26.20 PM.jpeg",
        "name": "Custom Clinic Sliding 'Doctor In' Door Sign",
        "desc": "Branded acrylic sliding nameplate with bold status indicators for private consultation cabins and clinics.",
        "type": "image"
    },
    {
        "id": 39,
        "cat": "new",
        "cat_name": "Latest Additions",
        "file": "thumbnail_video_1.jpg",
        "video_src": "catlogue/catlogue/WhatsApp Video 2026-09-10 at 3.24.23 PM.mp4",
        "name": "Executive Adjustable Wooden Mobile Stand",
        "desc": "Multi-angle foldable natural wood smartphone & tablet stand customized with laser-etched corporate logo.",
        "type": "video"
    },
    {
        "id": 40,
        "cat": "new",
        "cat_name": "Latest Additions",
        "file": "thumbnail_video_2.jpg",
        "video_src": "catlogue/catlogue/WhatsApp Video 2026-09-10 at 3.24.42 PM.mp4",
        "name": "Prestige Wooden Citation of Recognition Plaque",
        "desc": "Handcrafted dark wood beveled citation plaque with ornate laser-engraved birch faceplate and executive signatories.",
        "type": "video"
    },
    {
        "id": 41,
        "cat": "new",
        "cat_name": "Latest Additions",
        "file": "thumbnail_video_3.jpg",
        "video_src": "catlogue/catlogue/WhatsApp Video 2026-09-10 at 3.28.43 PM.mp4",
        "name": "Executive Sliding Door Status Indicator Sign",
        "desc": "Smooth dual-state 'Doctor In / Doctor Out' sliding cabin sign board with custom pharmaceutical sponsorship branding.",
        "type": "video"
    }
]

def generate_catalog_html():
    lines = []
    
    # Category Tabs
    lines.append('<div class="category-tabs" id="categoryTabs" role="tablist" aria-label="Product categories">')
    lines.append('  <button class="tab-btn active" role="tab" data-category="all" id="tab-all" aria-selected="true" aria-controls="catalog-grid">All</button>')
    for cat in categories_config:
        prefix = '✨ ' if cat['id'] == 'new' else ''
        lines.append(f'  <button class="tab-btn" role="tab" data-category="{cat["id"]}" id="tab-{cat["id"]}" aria-selected="false">{prefix}{cat["name"]}</button>')
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
            if p['type'] == 'video':
                video_attr = f'data-video="{p["video_src"]}" onclick="openVideoModal(this)" style="cursor:pointer"'
                lines.append(f'      <article class="product-card" id="product-{p["id"]}" data-animate="card" {video_attr}>')
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
            else:
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
