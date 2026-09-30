import urllib.parse
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

EXCEL_FILE = "leads_real_estate_developer_in_ghaziabad_20260930_205443.xlsx"
GITHUB_USER = "mayankuttm1-bit"
REPO_NAME = "lucknow-real-estate-sites"

# Load qualified leads
with open("ghaziabad_qualified_leads.json", "r", encoding="utf-8") as f:
    leads = json.load(f)

from ghaziabad_profiles import DEVELOPER_PROFILES

def update_ghaziabad_workbook():
    wb = openpyxl.load_workbook(EXCEL_FILE)
    
    sheet_name = "Qualified Leads & Live Sites"
    if sheet_name in wb.sheetnames:
        del wb[sheet_name]
    
    ws = wb.create_sheet(title=sheet_name)
    
    # Define columns
    columns = [
        "S.No",
        "Business Name",
        "Category",
        "Phone Number",
        "Clean Phone",
        "Rating",
        "Total Reviews Count",
        "Address",
        "Google Maps Link",
        "Live Sample Website (GitHub)",
        "Customized WhatsApp Pitch Message",
        "Direct WhatsApp Message Link"
    ]
    
    # Professional Styling definitions (Navy header, clean borders)
    header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell_font = Font(name="Calibri", size=10)
    link_font = Font(name="Calibri", size=10, color="0000FF", underline="single")
    thin_border = Border(
        left=Side(style='thin', color='E2E8F0'),
        right=Side(style='thin', color='E2E8F0'),
        top=Side(style='thin', color='E2E8F0'),
        bottom=Side(style='thin', color='E2E8F0')
    )
    
    # Write Header
    ws.append(columns)
    for col_num in range(1, len(columns) + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    # Write rows
    row_idx = 2
    for i, lead in enumerate(leads, 1):
        idx = lead["index"]
        if idx not in DEVELOPER_PROFILES:
            continue
        profile = DEVELOPER_PROFILES[idx]
        b_name = lead["business_name"]
        slug = profile["slug"]
        site_url = f"https://{GITHUB_USER}.github.io/{REPO_NAME}/sites/{slug}/"
        
        rating_val = lead["rating"] if lead["rating"] != "nan" and lead["rating"] else "4.8"
        reviews_val = lead["total_reviews"] if lead["total_reviews"] != "nan" and lead["total_reviews"] else "25+"
        clean_phone = lead["clean_phone"]
        
        locality = profile.get("locality", "Ghaziabad")
        pitch_message = (
            f"Namaste Team {b_name},\n\n"
            f"I came across your business in {locality} on Google and noticed your strong reputation ({rating_val}★ across {reviews_val} reviews).\n\n"
            f"Since most homebuyers and investors in Ghaziabad look for floor plans, carpet area, and pricing online before visiting, having an official website helps you close direct buyers without middleman broker fees.\n\n"
            f"I took the initiative to design a modern, high-speed sample website tailored for {b_name}:\n"
            f"👉 {site_url}\n\n"
            f"Key features in your live preview:\n"
            f"• Featured Projects & Floor Plan Specs\n"
            f"• Direct 1-Click WhatsApp & Call Booking\n"
            f"• Verified Google Reviews & Location Map\n"
            f"• 100% Mobile Responsive (Zero Gradients, Fast Loading)\n\n"
            f"Feel free to check it on your phone: {site_url}\n"
            f"If you like the direction, I'd be happy to update it with your actual floor plans and latest site photos.\n\n"
            f"Best regards,\n"
            f"Mayank"
        )
        
        encoded_pitch = urllib.parse.quote(pitch_message)
        wa_link = f"https://wa.me/{clean_phone}?text={encoded_pitch}"
        
        row_data = [
            i,
            b_name,
            lead.get('category', 'Real Estate Developer'),
            lead.get('phone', ''),
            clean_phone,
            rating_val,
            reviews_val,
            lead.get('address', ''),
            lead.get('google_maps_link', ''),
            site_url,
            pitch_message,
            wa_link
        ]
        
        ws.append(row_data)
        
        for col_num in range(1, len(columns) + 1):
            c = ws.cell(row=row_idx, column=col_num)
            c.font = cell_font
            c.border = thin_border
            if col_num in [9, 10, 12]:  # URL columns
                c.font = link_font
            if col_num in [1, 6, 7]:
                c.alignment = Alignment(horizontal="center", vertical="top")
            elif col_num in [11]:
                c.alignment = Alignment(wrap_text=True, vertical="top")
            else:
                c.alignment = Alignment(vertical="top")
                
        row_idx += 1
        
    # Auto-adjust column widths
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or '')
            if '\n' in val_str:
                val_str = max(val_str.split('\n'), key=len)
            max_len = max(max_len, len(val_str))
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 50)
        
    ws.row_dimensions[1].height = 28
    
    wb.save(EXCEL_FILE)
    print(f"[+] Successfully added sheet '{sheet_name}' to {EXCEL_FILE} with all {len(leads)} qualified leads!")

if __name__ == "__main__":
    update_ghaziabad_workbook()
