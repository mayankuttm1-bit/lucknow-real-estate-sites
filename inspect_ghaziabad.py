import pandas as pd

excel_file = 'leads_real_estate_developer_in_ghaziabad_20260930_205443.xlsx'
df = pd.read_excel(excel_file)

print(f"Total rows in Excel: {len(df)}")
print("Columns:", list(df.columns))

# Let's inspect rows with Has Website == 'No'
no_web = df[df['Has Website'].astype(str).str.strip().str.lower() == 'no'].copy()
print(f"\nTotal rows with Has Website == 'No': {len(no_web)}")

for idx, r in no_web.iterrows():
    bname = str(r['Business Name']).strip()
    phone = str(r.get('Phone Number', '')).strip()
    clean_phone = str(r.get('Clean Phone', '')).strip()
    rating = str(r.get('Rating', '')).strip()
    reviews = str(r.get('Total Reviews Count', '')).strip()
    addr = str(r.get('Address', '')).strip()
    maps_link = str(r.get('Google Maps Link', '')).strip()
    overview = str(r.get('Company Overview', '')).strip()
    owner = str(r.get('Owner Info', '')).strip()
    
    # Check if mobile no is available
    has_mobile = bool(phone and phone.lower() != 'nan' and phone != '')
    print(f"Row {idx} | Mobile Available: {has_mobile} | Name: {bname}")
    print(f"   Phone: {phone} | Clean: {clean_phone} | Rating: {rating} ({reviews})")
    print(f"   Address: {addr}")
    print(f"   Overview: {overview[:80]}...")
    print("-" * 60)

# Also check Social Only
social_web = df[df['Has Website'].astype(str).str.strip().str.lower() == 'social only'].copy()
print(f"\nTotal rows with Has Website == 'Social Only': {len(social_web)}")
for idx, r in social_web.iterrows():
    bname = str(r['Business Name']).strip()
    phone = str(r.get('Phone Number', '')).strip()
    web = str(r.get('Website URL', '')).strip()
    print(f"Social Row {idx} | Name: {bname} | Phone: {phone} | URL: {web}")
