import os

# Define categories and descriptions
categories = [
    {
        "id": "awards",
        "name": "Awards & Recognition",
        "tagline": "Honor the extraordinary with timeless mementos",
        "keywords": ["10.11"]
    },
    {
        "id": "heritage",
        "name": "Heritage & Commemorative",
        "tagline": "Marking history with premium displays",
        "keywords": ["10.13"]
    },
    {
        "id": "everyday",
        "name": "Everyday Utilities",
        "tagline": "Premium gifts for the journey and the routine",
        "keywords": ["5.40"]
    },
    {
        "id": "desk",
        "name": "Desk & Office",
        "tagline": "Elevate the workspace",
        "keywords": ["5.42"]
    },
    {
        "id": "custom",
        "name": "Bespoke & Customized Products",
        "tagline": "Tailor-made specifically for your brand",
        "keywords": ["ChatGPT", "05_52_26"]
    }
]

# Read all images
image_dir = r"e:\cat\catlogue\catlogue"
all_images = [f for f in os.listdir(image_dir) if f.endswith(('.jpeg', '.jpg', '.png'))]

# Generate product descriptions based on category
def get_product_details(cat_id, index):
    if cat_id == "awards":
        return {
            "name": f"Premium Recognition Trophy No. {index}",
            "desc": "A meticulously crafted award designed to honor outstanding achievements and milestones. Features premium materials and precision engraving for a lasting impression.",
            "specs": ["Material: Engineered wood & acrylic", "Customization: Precision laser engraving", "Finish: Hand-polished edges"]
        }
    elif cat_id == "heritage":
        return {
            "name": f"Commemorative Medallion Display {index}",
            "desc": "An elegant presentation of heritage. This set features die-struck medallions in a classic display frame, perfect for military, engineering, or lifetime honors.",
            "specs": ["Material: Die-struck metal alloy", "Frame: Classic oak-finish wood", "Mounting: Premium suede backing"]
        }
    elif cat_id == "everyday":
        return {
            "name": f"Signature Executive Utility {index}",
            "desc": "Built for the daily commute or the morning ritual. Crafted from durable, premium materials, this essential item seamlessly blends utility with sophisticated design.",
            "specs": ["Material: Water-resistant textiles / High-fired ceramic", "Durability: Built for everyday executive use", "Design: Minimalist and functional"]
        }
    elif cat_id == "custom":
        return {
            "name": f"Bespoke Customized Product {index}",
            "desc": "A fully tailored product designed exclusively around your brand guidelines. Features premium customization including precision engraving, custom colors, and personalized packaging.",
            "specs": ["Material: Custom selection (Metal, Leather, Ceramic)", "Customization: Logo Engraving, UV Print, Embossing", "Packaging: Bespoke rigid box"]
        }
    else:
        return {
            "name": f"Artisan Desk Organizer {index}",
            "desc": "A playful yet functional addition to any workspace. Precision-crafted to keep your essential tools organized while adding a touch of personality to your desk.",
            "specs": ["Material: Multi-layered wood veneer", "Functionality: Multi-tool organization", "Finish: Natural wood grain"]
        }

# Group images
grouped_images = {c["id"]: [] for c in categories}
for img in all_images:
    placed = False
    for cat in categories:
        for kw in cat["keywords"]:
            if kw in img:
                grouped_images[cat["id"]].append(img)
                placed = True
                break
        if placed:
            break
    if not placed:
        # Fallback
        grouped_images["desk"].append(img)

# Generate HTML
html = []

# Generate tabs
html.append('<div class="category-tabs" id="categoryTabs" role="tablist" aria-label="Product categories">')
html.append('<button class="tab-btn active" role="tab" data-category="all" id="tab-all" aria-selected="true" aria-controls="catalog-grid">All</button>')
for cat in categories:
    html.append(f'<button class="tab-btn" role="tab" data-category="{cat["id"]}" id="tab-{cat["id"]}" aria-selected="false">{cat["name"]}</button>')
html.append('</div>')

html.append('<div class="product-grid" id="catalog-grid" role="tabpanel">')

product_counter = 1
for cat in categories:
    html.append(f'<div class="category-block" data-category="{cat["id"]}">')
    html.append(f'<div class="category-title-bar">')
    html.append(f'<h3 class="category-name">{cat["name"]}</h3>')
    html.append(f'<span class="category-tagline">{cat["tagline"]}</span>')
    html.append(f'</div>')
    html.append('<div class="products-row">')
    
    for idx, img in enumerate(grouped_images[cat["id"]], 1):
        details = get_product_details(cat["id"], idx)
        
        html.append(f'<article class="product-card" id="product-{product_counter}" data-animate="card">')
        html.append(f'<div class="product-image-zone">')
        html.append(f'<img src="catlogue/catlogue/{img}" alt="{details["name"]}" class="product-photo" loading="lazy" />')
        html.append(f'<div class="product-num">S — {product_counter:02d}</div>')
        html.append(f'</div>')
        
        html.append(f'<div class="product-card-body">')
        html.append(f'<span class="product-category-tag">{cat["name"]}</span>')
        html.append(f'<h4 class="product-name">{details["name"]}</h4>')
        html.append(f'<p class="product-desc">{details["desc"]}</p>')
        
        html.append(f'</div>')
        html.append(f'</article>')
        
        product_counter += 1
        
    html.append('</div>') # end products-row
    html.append('</div>') # end category-block

html.append('</div>') # end product-grid

with open(r"e:\cat\generated_catalog.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html))

print("Done generating catalog HTML.")
