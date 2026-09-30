import os
import glob
import re

slugs = [
    "shri-khatu-shayam",
    "sk-developers",
    "gunnika-properties",
    "ghaziabad-properties",
    "horizon-heaven-estate",
    "sangam-properties",
    "goodwill-builders",
    "white-house-builders",
    "mangalam-properties"
]

all_passed = True
print("=== VERIFYING GHAZIABAD DEVELOPER SITES ===")

for slug in slugs:
    site_path = os.path.join("sites", slug, "index.html")
    if not os.path.exists(site_path):
        print(f"[FAIL] Missing {site_path}")
        all_passed = False
        continue

    with open(site_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Check for gradients
    if "gradient" in html.lower():
        print(f"[FAIL] Gradient detected in {slug}!")
        all_passed = False
    else:
        print(f"[PASS] No gradients in {slug}")

    # 2. Check stock images
    img_dir = os.path.join("sites", slug, "images")
    imgs = os.listdir(img_dir)
    if len(imgs) < 5:
        print(f"[FAIL] Less than 5 stock images in {slug}: {len(imgs)}")
        all_passed = False
    else:
        # Check all image sizes
        all_imgs_valid = True
        for im in imgs:
            im_path = os.path.join(img_dir, im)
            sz = os.path.getsize(im_path)
            if sz < 10000:
                print(f"[FAIL] Image {im} in {slug} is too small: {sz} bytes")
                all_imgs_valid = False
        if all_imgs_valid:
            print(f"[PASS] {len(imgs)} valid local stock images in {slug}")

    # 3. Check required sections
    required_sections = ["id=\"properties\"", "id=\"about\"", "id=\"services\"", "id=\"amenities\"", "id=\"reviews\"", "id=\"contact\""]
    missing_sections = [sec for sec in required_sections if sec not in html]
    if missing_sections:
        print(f"[FAIL] Missing sections in {slug}: {missing_sections}")
        all_passed = False
    else:
        print(f"[PASS] All required sections present in {slug}")

    # 4. Check showcase image
    showcase_path = os.path.join("images", "showcase", f"{slug}.jpg")
    if not os.path.exists(showcase_path) or os.path.getsize(showcase_path) < 10000:
        print(f"[FAIL] Missing showcase image for {slug}")
        all_passed = False
    else:
        print(f"[PASS] Showcase image present for {slug}")

    print("-" * 50)

if all_passed:
    print("\n>>> ALL CHECKS PASSED PERFECTLY FOR ALL 9 GHAZIABAD SITES! <<<")
else:
    print("\n>>> SOME CHECKS FAILED! <<<")
