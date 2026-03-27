# question_dataset.py

WEBSITE_QUESTION_DATASET = {

# ==========================================================
# 1️⃣ ECOMMERCE
# ==========================================================

"ecommerce": [

    # Business Model
    {"field": "target_audience", "question": "Target audience (B2B / B2C / Both)?"},
    {"field": "business_model", "question": "Business model (Single vendor / Multi-vendor marketplace)?"},
    {"field": "product_categories", "question": "Main product categories?"},
    {"field": "expected_scale", "question": "Expected scale (100 / 10k / 1M+ products)?"},
    {"field": "regional_scope", "question": "Selling region (Local / National / International)?"},

    # Homepage
    {"field": "homepage_sections", "question": "Homepage sections (Hero, Categories, Flash Sale, Testimonials, Brands)?"},
    {"field": "homepage_style", "question": "Homepage style (Minimal / Premium / Marketplace density)?"},
    {"field": "search_system", "question": "Search system (Basic / Autocomplete / AI search)?"},

    # Listing Page
    {"field": "listing_layout", "question": "Product listing layout (3-column / 4-column / Infinite scroll)?"},
    {"field": "filters", "question": "Filtering (Sidebar / Advanced multi-filter / Price slider / Ratings)?"},
    {"field": "sorting", "question": "Sorting options (Price / Popularity / Rating / AI ranking)?"},

    # Product Page
    {"field": "product_media", "question": "Product media (Carousel / Zoom / 360° view / Video demo)?"},
    {"field": "pricing_logic", "question": "Pricing (Fixed / Discount engine / Dynamic pricing)?"},
    {"field": "stock_logic", "question": "Stock management (Limited / Backorder / Preorder)?"},
    {"field": "recommendations", "question": "Recommendation system (Related / AI personalized)?"},
    {"field": "reviews", "question": "Review system (Star rating / Verified purchase / None)?"},

    # Cart & Checkout
    {"field": "cart_features", "question": "Cart features (Coupon / Save later / Auto-save)?"},
    {"field": "checkout_flow", "question": "Checkout (One-step / Multi-step / Express)?"},
    {"field": "shipping_logic", "question": "Shipping logic (Flat / Location-based / API integration)?"},
    {"field": "tax_logic", "question": "Tax calculation logic required? (Yes / No)"},

    # Payment
    {"field": "payment_methods", "question": "Payment methods (Card / UPI / Wallet / BNPL)?"},
    {"field": "payment_gateway", "question": "Preferred gateway (Stripe / Razorpay / PayPal)?"},
    {"field": "currency_support", "question": "Multi-currency support? (Yes / No)"},

    # Accounts
    {"field": "authentication", "question": "Authentication (Email / Google / OTP / Social login)?"},
    {"field": "user_dashboard", "question": "User dashboard features (Orders / Wishlist / Returns)?"},
    {"field": "returns_management", "question": "Returns management required? (Yes / No)"},

    # Admin
    {"field": "admin_features", "question": "Admin features (Product CRUD / Orders / Vendors / Analytics)?"},
    {"field": "analytics", "question": "Analytics level (Basic / Sales dashboard / Enterprise BI)?"},
    {"field": "inventory_automation", "question": "Inventory automation needed? (Yes / No)"},

    # Technical
    {"field": "design_level", "question": "Design level (Standard / Premium / Enterprise)?"},
    {"field": "frontend", "question": "Frontend (React / Next.js / Vue)?"},
    {"field": "backend", "question": "Backend (Node / Django / FastAPI)?"},
    {"field": "database", "question": "Database (MongoDB / PostgreSQL / MySQL)?"},
    {"field": "hosting", "question": "Hosting (AWS / GCP / Azure)?"},
    {"field": "performance_priority", "question": "Performance priority (Standard / High / CDN optimized)?"}
],

# ==========================================================
# 2️⃣ SAAS
# ==========================================================

"saas": [

    {"field": "product_type", "question": "What type of SaaS (CRM / AI Tool / Analytics / Project Management)?"},
    {"field": "target_users", "question": "Target users (Startups / Enterprises / Individuals)?"},
    {"field": "subscription_model", "question": "Subscription model (Free / Tiered / Enterprise)?"},
    {"field": "billing_cycle", "question": "Billing cycle (Monthly / Yearly / Usage-based)?"},
    {"field": "dashboard_complexity", "question": "Dashboard complexity (Basic / Advanced analytics)?"},
    {"field": "role_management", "question": "Role-based access control needed? (Yes / No)"},
    {"field": "api_access", "question": "Public API access required? (Yes / No)"},
    {"field": "multi_tenant", "question": "Multi-tenant architecture needed? (Yes / No)"},
    {"field": "security_level", "question": "Security level (Standard / Enterprise / SOC2-ready)?"},
    {"field": "data_encryption", "question": "Data encryption required? (Yes / No)"},
    {"field": "scalability", "question": "Expected user scale (1k / 100k / 1M+)?"},
    {"field": "hosting", "question": "Hosting preference?"}
],

# ==========================================================
# 3️⃣ PORTFOLIO
# ==========================================================

"portfolio": [

    {"field": "profession", "question": "Profession (Developer / Designer / Photographer etc)?"},
    {"field": "design_style", "question": "Design style (Minimal / Creative / 3D / Animated)?"},
    {"field": "sections", "question": "Sections (About / Projects / Blog / Testimonials / Contact)?"},
    {"field": "project_showcase", "question": "Project showcase style (Grid / Case study pages)?"},
    {"field": "animations", "question": "Advanced animations needed? (Yes / No)"},
    {"field": "blog_integration", "question": "Blog integration required? (Yes / No)"},
    {"field": "resume_download", "question": "Resume download required?"},
    {"field": "contact_form", "question": "Contact integration (Email / CRM)?"},
    {"field": "theme", "question": "Theme (Dark / Light / Auto)?"},
    {"field": "seo_priority", "question": "SEO optimization required? (Basic / Advanced)?"},
    {"field": "hosting", "question": "Hosting preference?"}
],

# ==========================================================
# 4️⃣ BLOG
# ==========================================================

"blog": [

    {"field": "blog_type", "question": "Blog type (Personal / Tech / News)?"},
    {"field": "content_frequency", "question": "Publishing frequency?"},
    {"field": "cms", "question": "CMS (Custom admin / Headless CMS)?"},
    {"field": "monetization", "question": "Monetization (Ads / Subscription / Premium)?"},
    {"field": "comment_system", "question": "Comment system (Native / Disqus)?"},
    {"field": "newsletter", "question": "Newsletter integration required?"},
    {"field": "seo_level", "question": "SEO level (Basic / Advanced / Enterprise)?"},
    {"field": "analytics", "question": "Analytics integration required?"},
    {"field": "hosting", "question": "Hosting preference?"}
],

# ==========================================================
# 5️⃣ CORPORATE
# ==========================================================

"corporate": [

    {"field": "company_type", "question": "Company type (Startup / Enterprise / Agency)?"},
    {"field": "pages", "question": "Pages needed (Home / About / Services / Careers / Blog)?"},
    {"field": "design_level", "question": "Design level (Professional / Premium)?"},
    {"field": "crm_integration", "question": "CRM integration required?"},
    {"field": "lead_generation", "question": "Lead generation forms required?"},
    {"field": "multi_language", "question": "Multi-language support needed?"},
    {"field": "seo_level", "question": "SEO level required?"},
    {"field": "hosting", "question": "Hosting preference?"}
],

# ==========================================================
# 6️⃣ SOCIAL MEDIA
# ==========================================================

"social_media": [

    {"field": "platform_type", "question": "Platform type (Photo / Video / Community)?"},
    {"field": "real_time", "question": "Real-time chat required?"},
    {"field": "feed_algorithm", "question": "Feed system (Chronological / Algorithmic)?"},
    {"field": "content_moderation", "question": "Content moderation required?"},
    {"field": "scalability", "question": "Expected users (1k / 100k / 1M+)?"},
    {"field": "authentication", "question": "Authentication type?"},
    {"field": "database", "question": "Database preference?"},
    {"field": "hosting", "question": "Hosting preference?"}
],

# ==========================================================
# 7️⃣ REAL ESTATE
# ==========================================================

"real_estate": [

    {"field": "property_type", "question": "Property types (Residential / Commercial)?"},
    {"field": "map_integration", "question": "Map integration required?"},
    {"field": "advanced_filters", "question": "Advanced search filters required?"},
    {"field": "agent_profiles", "question": "Agent profiles required?"},
    {"field": "booking_system", "question": "Property visit booking system needed?"},
    {"field": "analytics", "question": "Analytics dashboard required?"},
    {"field": "hosting", "question": "Hosting preference?"}
],

# ==========================================================
# 8️⃣ JOB PORTAL
# ==========================================================

"job_portal": [

    {"field": "user_types", "question": "User types (Job seeker / Employer / Both)?"},
    {"field": "resume_upload", "question": "Resume upload required?"},
    {"field": "job_posting_dashboard", "question": "Employer dashboard needed?"},
    {"field": "search_filters", "question": "Advanced job filters required?"},
    {"field": "subscription_model", "question": "Paid job posting model required?"},
    {"field": "analytics", "question": "Analytics required?"},
    {"field": "hosting", "question": "Hosting preference?"}
]

}