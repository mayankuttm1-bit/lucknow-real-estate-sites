import pandas as pd
import json

excel_file = 'leads_real_estate_developers_in_lucknow_20260929_204339.xlsx'
df = pd.read_excel(excel_file)
no_web = df[df['Has Website'].astype(str).str.strip().str.lower() == 'no']

leads_data = []
for i, r in no_web.reset_index(drop=True).iterrows():
    lead = {
        'id': i + 1,
        'business_name': str(r['Business Name']).strip(),
        'category': str(r.get('Category', '')),
        'phone': str(r.get('Phone Number', '')),
        'clean_phone': str(r.get('Clean Phone', '')),
        'rating': str(r.get('Rating', '')),
        'reviews_count': str(r.get('Total Reviews Count', '')),
        'address': str(r.get('Address', '')),
        'google_maps_link': str(r.get('Google Maps Link', '')),
        'company_overview': str(r.get('Company Overview', '')),
        'owner_info': str(r.get('Owner Info', ''))
    }
    leads_data.append(lead)
    print(f"=== #{lead['id']}: {lead['business_name']} ===")
    print(f"  Phone: {lead['phone']} | Clean: {lead['clean_phone']}")
    print(f"  Rating: {lead['rating']} | Reviews: {lead['reviews_count']}")
    print(f"  Address: {lead['address']}")
    print(f"  Maps Link: {lead['google_maps_link']}")
    print(f"  Overview: {lead['company_overview'][:100]}...")
    print()

with open('selected_10_leads.json', 'w', encoding='utf-8') as f:
    json.dump(leads_data, f, indent=2, ensure_ascii=False)
