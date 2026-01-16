import pandas as pd
import json
import re

input_json = '/Users/bimaaristo/MH/data/revise/add-on-v2.json'
output_excel = '/Users/bimaaristo/MH/src/proposed_matrix_structure.xlsx'

# --- 1. Define the Schema & Logic ---
# Structure: Main Attribute -> {Sub-Attribute: [Keywords]}
schema = {
    "Field Extraction": {
        "Price / Amount": ["price", "amount", "rate", "tax", "total", "cost", "value", "pricing"],
        "Quantity": ["qty", "quantity", "volume", "weight"],
        "Dates": ["date", "arrival", "year", "month", "time"],
        "Codes / IDs": ["sku", "number", "no", "code", "permit", "license", "id"],
        "Description": ["description", "text", "brand", "name", "desc"]
    },
    "Automation / AI": {
        "Extraction (OCR)": ["extract", "ocr", "read", "recognition"],
        "Validation / Matching": ["validate", "compare", "match", "check", "reconcile", "verify", "validation"],
        "Classification": ["classify", "sort", "filter", "route", "segregate"],
        "Generation / Creation": ["create", "generate", "populate", "merge", "compile"],
        "Translation": ["translate", "translation"]
    },
    "Source System": {
        "PDF Document": ["pdf", "scanned", "scan"],
        "Excel File": ["excel", "spreadsheet", "xls", "csv"],
        "Email": ["email", "mailbox"],
        "SAP / ERP": ["sap", "me21n", "erp"],
        "Web / Portal": ["portal", "website", "online", "web"]
    },
    "Target System": {
        "Excel Report": ["excel", "calculation", "tracker", "sheet", "dashboard"],
        "SAP / ERP": ["sap", "po", "shipment", "sp0"],
        "Email Notification": ["email", "notify", "send"],
        "File Storage": ["folder", "drive", "sharepoint", "save"]
    }
}

def check_keywords(text, keywords):
    if not isinstance(text, str):
        return False
    text = text.lower()
    for k in keywords:
        if k in text:
            return True
    return False

try:
    with open(input_json, 'r') as f:
        data = json.load(f)

    # --- 2. Build the Matrix Data ---
    matrix_rows = []
    
    for item in data:
        row = {
            "Department": item.get('Department', ''),
            "Topic": item.get('Topic', ''),
            "Description": item.get('Description', '') + " " + str(item.get('Remarks', ''))
        }
        
        # Combine text for analysis
        full_text = row["Description"]
        
        for main_attr, sub_attrs in schema.items():
            for sub_name, keywords in sub_attrs.items():
                col_name = f"{main_attr} - {sub_name}"
                is_present = check_keywords(full_text, keywords)
                row[col_name] = "Yes" if is_present else "No"
                
        matrix_rows.append(row)

    df_matrix = pd.DataFrame(matrix_rows)

    # --- 3. Build the Definitions Data ---
    def_rows = []
    for main_attr, sub_attrs in schema.items():
        for sub_name, keywords in sub_attrs.items():
            def_rows.append({
                "Main Attribute": main_attr,
                "Sub-Attribute": sub_name,
                "Logic (Keywords)": ", ".join(keywords)
            })
    df_defs = pd.DataFrame(def_rows)

    # --- 4. Export to Excel ---
    with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
        # Sheet 1: Definitions
        df_defs.to_excel(writer, sheet_name='Definitions', index=False)
        worksheet1 = writer.sheets['Definitions']
        worksheet1.set_column(0, 0, 25)
        worksheet1.set_column(1, 1, 25)
        worksheet1.set_column(2, 2, 50)
        
        # Sheet 2: Matrix Preview
        df_matrix.to_excel(writer, sheet_name='Matrix Preview', index=False)
        worksheet2 = writer.sheets['Matrix Preview']
        
        # Format Matrix
        worksheet2.set_column(0, 1, 20) # Dept, Topic
        worksheet2.set_column(2, 2, 40) # Description
        # Columns for logic
        for i in range(3, len(df_matrix.columns)):
            worksheet2.set_column(i, i, 15)

    print(f"Propsoed Matrix Report generated at: {output_excel}")

except Exception as e:
    print(f"Error generating matrix: {e}")
