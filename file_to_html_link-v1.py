import pandas as pd

# 1. Load the data
df = pd.read_csv('company_research.csv')

# 2. Function to format links and handle empty values
def format_links(val):
    if pd.isna(val) or not str(val).startswith('http'):
        return "" if pd.isna(val) else val
    # Keep URL short for display if it's very long
    display = str(val)[:50] + "..." if len(str(val)) > 50 else val
    return f'<a href="{val}" target="_blank">{display}</a>'

# 3. Apply formatting to columns
for col in ['Website', 'LinkedIn', 'Facebook', 'X_Twitter']:
    if col in df.columns:
        df[col] = df[col].apply(format_links)

df = df.fillna("") # Clean up any other empty cells

# 4. Generate the HTML with modern CSS
html_table = df.to_html(index=False, escape=False, classes='modern-table')

full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Company Research Database</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f4f7f6; padding: 40px; }}
        .container {{ max-width: 1400px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
        h1 {{ text-align: center; color: #2c3e50; }}
        .modern-table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        .modern-table thead tr {{ background-color: #2c3e50; color: white; text-align: left; }}
        .modern-table th, .modern-table td {{ padding: 12px 15px; border-bottom: 1px solid #e0e0e0; }}
        .modern-table tbody tr:nth-of-type(even) {{ background-color: #f9f9f9; }}
        .modern-table tbody tr:hover {{ background-color: #f1f1f1; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Company Research Database</h1>
        {html_table}
    </div>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)