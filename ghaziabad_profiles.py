import os
import shutil
import json

# Load qualified leads
with open("ghaziabad_qualified_leads.json", "r", encoding="utf-8") as f:
    leads = json.load(f)

# Define developer specific metadata & slugs
DEVELOPER_PROFILES = {
    0: {
        "slug": "shri-khatu-shayam",
        "short_name": "Shri Khatu Shayam",
        "tagline": "Premium Residential Townships & Prime Freehold Land in Duhai",
        "locality": "Duhai, RRTS Corridor",
        "experience": "14+ Years",
        "projects_count": "18+ Delivered",
        "happy_families": "1,200+",
        "sqft_delivered": "2.4M+ Sq. Ft.",
        "accent_color": "#1E3A8A", # Solid Navy
        "accent_bg": "#EFF6FF",
        "accent_border": "#BFDBFE",
        "hero_img": "arch-hero-1.jpg",
        "about_img": "about-arch-1.jpg",
        "projects": [
            {
                "title": "Shyam Enclave Heights",
                "type": "Luxury Residential Floors",
                "config": "2 & 3 BHK Luxury Floors",
                "area": "1,150 - 1,650 sq.ft.",
                "price": "₹48 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-res-1.jpg"
            },
            {
                "title": "Duhai Green Township",
                "type": "Gated Plotted Development",
                "config": "100 - 250 Sq. Yds. Freehold Plots",
                "area": "Gated Township with Park",
                "price": "₹32 Lakh* onwards",
                "status": "Newly Launched",
                "img": "prop-plot-1.jpg"
            },
            {
                "title": "Khatu Shayam Commercial Arcade",
                "type": "High-Street Retail & Offices",
                "config": "Retail Shops & Office Spaces",
                "area": "350 - 1,200 sq.ft.",
                "price": "₹55 Lakh* onwards",
                "status": "Under Construction",
                "img": "prop-comm-1.jpg"
            }
        ]
    },
    2: {
        "slug": "sk-developers",
        "short_name": "SK Developers",
        "tagline": "Engineered Modern Living & Urban Infrastructure in Lal Kuan",
        "locality": "Lal Kuan, GT Road NH-9",
        "experience": "12+ Years",
        "projects_count": "15+ Completed",
        "happy_families": "950+",
        "sqft_delivered": "1.8M+ Sq. Ft.",
        "accent_color": "#047857", # Solid Emerald
        "accent_bg": "#ECFDF5",
        "accent_border": "#A7F3D0",
        "hero_img": "arch-hero-2.jpg",
        "about_img": "about-arch-2.jpg",
        "projects": [
            {
                "title": "SK Tower Residency",
                "type": "Modern High-Rise Apartments",
                "config": "2 & 3 BHK Premium Suites",
                "area": "1,220 - 1,780 sq.ft.",
                "price": "₹52 Lakh* onwards",
                "status": "Under Construction",
                "img": "prop-res-2.jpg"
            },
            {
                "title": "Shankar Vihar Executive Floors",
                "type": "Independent Builder Floors",
                "config": "3 BHK Low-Rise Luxury",
                "area": "1,500 sq.ft.",
                "price": "₹62 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-floor-1.jpg"
            },
            {
                "title": "SK Commercial Complex",
                "type": "Grade-A Retail Plaza",
                "config": "Showrooms & Corporate Suites",
                "area": "450 - 2,100 sq.ft.",
                "price": "₹45 Lakh* onwards",
                "status": "Near Possession",
                "img": "prop-comm-2.jpg"
            }
        ]
    },
    3: {
        "slug": "gunnika-properties",
        "short_name": "Gunnika Developers",
        "tagline": "Curated Gated Communities & Bespoke Homes in Kailash Puram",
        "locality": "Sadarpur & Govindpuram",
        "experience": "15+ Years",
        "projects_count": "20+ Projects",
        "happy_families": "1,500+",
        "sqft_delivered": "3.1M+ Sq. Ft.",
        "accent_color": "#92400E", # Solid Amber Bronze
        "accent_bg": "#FFFBEB",
        "accent_border": "#FDE68A",
        "hero_img": "arch-hero-3.jpg",
        "about_img": "about-arch-1.jpg",
        "projects": [
            {
                "title": "Gunnika Royal Palm",
                "type": "Luxury Family Residences",
                "config": "3 & 4 BHK Sunlit Apartments",
                "area": "1,450 - 2,250 sq.ft.",
                "price": "₹68 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-res-3.jpg"
            },
            {
                "title": "Kailash Puram Greens",
                "type": "Modern Townhomes & Floors",
                "config": "2 & 3 BHK Independent Floors",
                "area": "1,180 - 1,600 sq.ft.",
                "price": "₹46 Lakh* onwards",
                "status": "Phase 2 Ongoing",
                "img": "prop-floor-2.jpg"
            },
            {
                "title": "Gunnika Avenue Retail",
                "type": "Community Shopping Arcade",
                "config": "Corner Commercial Outlets",
                "area": "300 - 850 sq.ft.",
                "price": "₹38 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-comm-1.jpg"
            }
        ]
    },
    5: {
        "slug": "ghaziabad-properties",
        "short_name": "Ghaziabad Properties",
        "tagline": "Industrial Logistics Hubs & Prime Commercial Estates",
        "locality": "Pandav Nagar & Diamond Flyover",
        "experience": "18+ Years",
        "projects_count": "32+ Projects",
        "happy_families": "600+ Corporate Clients",
        "sqft_delivered": "5.5M+ Sq. Ft.",
        "accent_color": "#0F172A", # Solid Slate Dark
        "accent_bg": "#F8FAFC",
        "accent_border": "#E2E8F0",
        "hero_img": "arch-hero-5.jpg",
        "about_img": "about-arch-3.jpg",
        "projects": [
            {
                "title": "Diamond Industrial Logistics Park",
                "type": "Grade-A Warehouses & Sheds",
                "config": "5,000 - 45,000 sq.ft. Heavy Plates",
                "area": "High Ceiling, Heavy DG Backup",
                "price": "Custom Lease & Sale",
                "status": "Ready for Occupation",
                "img": "prop-comm-1.jpg"
            },
            {
                "title": "Pandav Commercial Complex",
                "type": "Corporate IT & Commercial Hub",
                "config": "Office Floors & Retail Frontage",
                "area": "800 - 4,500 sq.ft.",
                "price": "₹75 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-comm-2.jpg"
            },
            {
                "title": "Highway Industrial Enclave",
                "type": "Clear-Title Industrial Plots",
                "config": "500 - 2,000 Sq. Mtrs. Plots",
                "area": "Wide Road Connectivity",
                "price": "₹1.10 Cr* onwards",
                "status": "Immediate Registry",
                "img": "prop-plot-1.jpg"
            }
        ]
    },
    6: {
        "slug": "horizon-heaven-estate",
        "short_name": "Horizon Heaven",
        "tagline": "Architectural Elegance & Luxury Urban Residences in Nehru Nagar",
        "locality": "Nehru Nagar III, Central Ghaziabad",
        "experience": "16+ Years",
        "projects_count": "22+ Developments",
        "happy_families": "1,800+",
        "sqft_delivered": "3.8M+ Sq. Ft.",
        "accent_color": "#1E3A8A", # Solid Deep Blue
        "accent_bg": "#EFF6FF",
        "accent_border": "#BFDBFE",
        "hero_img": "arch-hero-4.jpg",
        "about_img": "about-arch-2.jpg",
        "projects": [
            {
                "title": "Horizon Heaven Sky Suites",
                "type": "Ultra-Luxury High-Rise",
                "config": "3 & 4 BHK Sky Condos",
                "area": "1,850 - 2,900 sq.ft.",
                "price": "₹1.25 Cr* onwards",
                "status": "Near Possession",
                "img": "prop-res-1.jpg"
            },
            {
                "title": "Nehru Enclave Boutique Residences",
                "type": "Low-Density Builder Floors",
                "config": "3 BHK + Private Terrace",
                "area": "1,750 sq.ft.",
                "price": "₹95 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-floor-1.jpg"
            },
            {
                "title": "Horizon Corporate Tower",
                "type": "Modern Office Suites",
                "config": "Flexible Corporate Floor Plates",
                "area": "600 - 3,500 sq.ft.",
                "price": "₹80 Lakh* onwards",
                "status": "Under Construction",
                "img": "prop-comm-2.jpg"
            }
        ]
    },
    7: {
        "slug": "sangam-properties",
        "short_name": "Sangam Properties",
        "tagline": "Trusted Commercial Centers & Prime Residential Spaces in Mohan Nagar",
        "locality": "Mohan Nagar & Sahibabad",
        "experience": "20+ Years",
        "projects_count": "45+ Completed",
        "happy_families": "3,200+",
        "sqft_delivered": "6.2M+ Sq. Ft.",
        "accent_color": "#1E3A8A", # Solid Corporate Navy
        "accent_bg": "#EFF6FF",
        "accent_border": "#BFDBFE",
        "hero_img": "arch-hero-1.jpg",
        "about_img": "about-arch-3.jpg",
        "projects": [
            {
                "title": "Sangam Metro Heights",
                "type": "Transit-Oriented Residences",
                "config": "2, 3 & 4 BHK Modern Apartments",
                "area": "1,250 - 2,150 sq.ft.",
                "price": "₹65 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-res-2.jpg"
            },
            {
                "title": "Rajendra Nagar Commercial Arcade",
                "type": "Prime High-Street Retail",
                "config": "Anchor Stores & Retail Outlets",
                "area": "300 - 1,800 sq.ft.",
                "price": "₹50 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-comm-1.jpg"
            },
            {
                "title": "Sangam Executive Park",
                "type": "Industrial & Office Hub",
                "config": "Grade-A Workspaces",
                "area": "1,000 - 8,000 sq.ft.",
                "price": "₹90 Lakh* onwards",
                "status": "Ongoing Expansion",
                "img": "prop-comm-2.jpg"
            }
        ]
    },
    9: {
        "slug": "goodwill-builders",
        "short_name": "Goodwill Builders",
        "tagline": "Quality Construction & Transparent Family Homes in Panchwati",
        "locality": "Panchwati Colony, Bhatia Mod",
        "experience": "14+ Years",
        "projects_count": "16+ Delivered",
        "happy_families": "850+",
        "sqft_delivered": "1.6M+ Sq. Ft.",
        "accent_color": "#065F46", # Solid Forest Emerald
        "accent_bg": "#ECFDF5",
        "accent_border": "#A7F3D0",
        "hero_img": "arch-hero-2.jpg",
        "about_img": "about-arch-2.jpg",
        "projects": [
            {
                "title": "Goodwill Panchwati Residency",
                "type": "Spacious Family Apartments",
                "config": "2 & 3 BHK Vastu-Compliant Homes",
                "area": "1,100 - 1,550 sq.ft.",
                "price": "₹45 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-res-3.jpg"
            },
            {
                "title": "Goodwill City Floors",
                "type": "Independent Builder Floors",
                "config": "3 BHK Floors with Dedicated Lift",
                "area": "1,350 sq.ft.",
                "price": "₹58 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-floor-2.jpg"
            },
            {
                "title": "Goodwill Market Square",
                "type": "Retail & Neighborhood Shops",
                "config": "Convenience Retail Units",
                "area": "200 - 600 sq.ft.",
                "price": "₹28 Lakh* onwards",
                "status": "Near Handover",
                "img": "prop-comm-1.jpg"
            }
        ]
    },
    10: {
        "slug": "white-house-builders",
        "short_name": "White House Builders",
        "tagline": "Ultra-Luxury Bespoke Builder Floors in Indirapuram",
        "locality": "Gyan Khand, Indirapuram",
        "experience": "16+ Years",
        "projects_count": "24+ Boutique Projects",
        "happy_families": "700+ Luxury Clients",
        "sqft_delivered": "2.1M+ Sq. Ft.",
        "accent_color": "#18181B", # Solid Zinc Dark Luxury
        "accent_bg": "#F4F4F5",
        "accent_border": "#E4E4E7",
        "hero_img": "arch-hero-4.jpg",
        "about_img": "about-arch-1.jpg",
        "projects": [
            {
                "title": "White House Signature Floors",
                "type": "Luxury Gated Builder Floors",
                "config": "3 & 4 BHK Italian Marble Suites",
                "area": "1,850 - 2,600 sq.ft.",
                "price": "₹1.40 Cr* onwards",
                "status": "Ready to Move",
                "img": "prop-floor-1.jpg"
            },
            {
                "title": "Gyan Khand Villa Mansions",
                "type": "Independent Luxury Villas",
                "config": "4 BHK Duplex with Private Garden",
                "area": "2,800 sq.ft.",
                "price": "₹2.25 Cr* onwards",
                "status": "Limited Units",
                "img": "prop-floor-2.jpg"
            },
            {
                "title": "White House Elite Penthouse",
                "type": "Sky Villa with Rooftop Deck",
                "config": "4 BHK + Maid Room + Terrace",
                "area": "3,400 sq.ft.",
                "price": "₹2.80 Cr* onwards",
                "status": "Ready to Move",
                "img": "prop-res-1.jpg"
            }
        ]
    },
    11: {
        "slug": "mangalam-properties",
        "short_name": "Mangalam Properties",
        "tagline": "Govindpuram's Premier Developer for Gated Townships & Freehold Homes",
        "locality": "Govindpuram & Signature Street",
        "experience": "18+ Years",
        "projects_count": "35+ Completed",
        "happy_families": "2,800+",
        "sqft_delivered": "4.5M+ Sq. Ft.",
        "accent_color": "#B45309", # Solid Warm Ochre Bronze
        "accent_bg": "#FEF3C7",
        "accent_border": "#FDE68A",
        "hero_img": "arch-hero-3.jpg",
        "about_img": "about-arch-2.jpg",
        "projects": [
            {
                "title": "Mangalam Signature Enclave",
                "type": "Gated High-Rise Residential",
                "config": "2 & 3 BHK Scenic Apartments",
                "area": "1,150 - 1,720 sq.ft.",
                "price": "₹49 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-res-2.jpg"
            },
            {
                "title": "Govindpuram Royal Villas",
                "type": "Custom Built Duplex Villas",
                "config": "3 & 4 BHK Independent Kothis",
                "area": "1,600 - 2,400 sq.ft.",
                "price": "₹78 Lakh* onwards",
                "status": "Under Construction",
                "img": "prop-floor-1.jpg"
            },
            {
                "title": "Mangalam Commercial Galleria",
                "type": "Commercial High-Street Plaza",
                "config": "Retail Showrooms & Offices",
                "area": "350 - 1,500 sq.ft.",
                "price": "₹42 Lakh* onwards",
                "status": "Ready to Move",
                "img": "prop-comm-1.jpg"
            }
        ]
    }
}

print(f"Profile configurations ready for all {len(DEVELOPER_PROFILES)} qualified leads.")
