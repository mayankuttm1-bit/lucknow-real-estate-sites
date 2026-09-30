import os
import urllib.request
import time

# List of high-quality architectural, residential, commercial real estate photos from Unsplash
IMAGE_CATALOG = {
    "arch-hero-1.jpg": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1400&q=80", # Luxury apartment complex
    "arch-hero-2.jpg": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1400&q=80", # Modern luxury villa
    "arch-hero-3.jpg": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1400&q=80", # Modern residence with pool
    "arch-hero-4.jpg": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1400&q=80", # Luxury architectural home
    "arch-hero-5.jpg": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1400&q=80", # Modern commercial tower
    "about-arch-1.jpg": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1000&q=80", # Architecture planning & blueprints
    "about-arch-2.jpg": "https://images.unsplash.com/photo-1541888946425-d0fbb186156f?auto=format&fit=crop&w=1000&q=80", # Construction engineering
    "about-arch-3.jpg": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1000&q=80", # Modern corporate architectural office
    "prop-res-1.jpg": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1000&q=80", # Residential tower
    "prop-res-2.jpg": "https://images.unsplash.com/photo-1600565193348-f74bd3c7ccdf?auto=format&fit=crop&w=1000&q=80", # Modern interior living
    "prop-res-3.jpg": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1000&q=80", # Luxury dining & balcony
    "prop-comm-1.jpg": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=80", # Commercial facade
    "prop-comm-2.jpg": "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1000&q=80", # Commercial retail / office
    "prop-floor-1.jpg": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=1000&q=80", # Builder floors exterior
    "prop-floor-2.jpg": "https://images.unsplash.com/photo-1600573472550-8090b5e0745e?auto=format&fit=crop&w=1000&q=80", # Luxury patio & lawn
    "prop-plot-1.jpg": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1000&q=80", # Green land / township plots
    "amenity-club.jpg": "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&w=1000&q=80", # Swimming pool & club
    "amenity-gym.jpg": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1000&q=80", # Modern fitness gym
    "amenity-park.jpg": "https://images.unsplash.com/photo-1584467735871-8e85353a8413?auto=format&fit=crop&w=1000&q=80" # Landscaped green park
}

os.makedirs("stock_cache", exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in IMAGE_CATALOG.items():
    dest = os.path.join("stock_cache", fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f"[OK] Cached: {fname} ({os.path.getsize(dest)} bytes)")
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(dest, "wb") as f:
                f.write(data)
            print(f"[Downloaded] {fname} ({len(data)} bytes)")
        time.sleep(0.5)
    except Exception as e:
        print(f"[Error] Failed {fname}: {e}")

print("Image catalog processing complete!")
