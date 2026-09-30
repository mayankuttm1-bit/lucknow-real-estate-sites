import pandas as pd
import json

excel_file = 'leads_real_estate_developer_in_ghaziabad_20260930_205443.xlsx'
df = pd.read_excel(excel_file)

leads = []
for idx, r in df.iterrows():
    has_web = str(r.get('Has Website', '')).strip().lower()
    phone = str(r.get('Phone Number', '')).strip()
    if (has_web in ['no', 'social only']) and phone and phone.lower() != 'nan':
        leads.append({
            'index': idx,
            'business_name': str(r.get('Business Name', '')).strip(),
            'category': str(r.get('Category', 'Real Estate Developer')).strip(),
            'company_overview': str(r.get('Company Overview', '')).strip(),
            'owner_info': str(r.get('Owner Info', '')).strip(),
            'email': str(r.get('Email ID', '')).strip(),
            'phone': str(r.get('Phone Number', '')).strip(),
            'clean_phone': str(r.get('Clean Phone', '')).replace('.0', '').strip(),
            'has_website': str(r.get('Has Website', '')).strip(),
            'website_url': str(r.get('Website URL', '')).strip(),
            'rating': str(r.get('Rating', '')).strip(),
            'total_reviews': str(r.get('Total Reviews Count', '')).strip(),
            'address': str(r.get('Address', '')).strip(),
            'google_maps_link': str(r.get('Google Maps Link', '')).strip()
        })

print(f"Total qualified leads: {len(leads)}")
with open('ghaziabad_qualified_leads.json', 'w', encoding='utf-8') as f:
    json.dump(leads, f, indent=2, ensure_ascii=False)

for l in leads:
    print(f"- {l['business_name']} | Phone: {l['phone']} | Rating: {l['rating']} ({l['total_reviews']}) | Addr: {l['address']}")
