import pandas as pd

excel_file = 'leads_real_estate_developer_in_ghaziabad_20260930_205443.xlsx'
df = pd.read_excel(excel_file)

print(df[['Business Name', 'Has Website', 'Phone Number', 'Rating', 'Total Reviews Count']])
