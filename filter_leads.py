import pandas as pd

excel_file = 'leads_real_estate_developer_in_ghaziabad_20260930_205443.xlsx'
df = pd.read_excel(excel_file)

print("--- Strict Has Website == 'No' AND Phone is not null ---")
cond_no = (df['Has Website'].astype(str).str.strip().str.lower() == 'no') & (df['Phone Number'].notna()) & (df['Phone Number'].astype(str).str.strip().str.lower() != 'nan') & (df['Phone Number'].astype(str).str.strip() != '')
filtered_no = df[cond_no]
print(f"Count: {len(filtered_no)}")
for idx, r in filtered_no.iterrows():
    print(f"Idx {idx} | {r['Business Name']} | Phone: {r['Phone Number']} | Clean: {r['Clean Phone']}")

print("\n--- Also including Social Only if applicable ---")
cond_soc = (df['Has Website'].astype(str).str.strip().str.lower() == 'social only') & (df['Phone Number'].notna()) & (df['Phone Number'].astype(str).str.strip().str.lower() != 'nan')
filtered_soc = df[cond_soc]
for idx, r in filtered_soc.iterrows():
    print(f"Social Idx {idx} | {r['Business Name']} | Phone: {r['Phone Number']} | Clean: {r['Clean Phone']}")
