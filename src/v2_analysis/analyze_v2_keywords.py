import json
import re
from collections import Counter

file_path = '/Users/bimaaristo/MH/data/revise/add-on-v2.json'

def get_keywords(text):
    if not text or not isinstance(text, str):
        return []
    # simple splitting
    words = re.findall(r'\w+', text.lower())
    return words

try:
    with open(file_path, 'r') as f:
        data = json.load(f)

    descriptions = []
    remarks = []
    
    for item in data:
        descriptions.append(str(item.get('Description', '')))
        remarks.append(str(item.get('Remarks', '')))
        
    all_text = " ".join(descriptions + remarks)
    
    # Analyze common terms for Fields
    field_terms = ['price', 'amount', 'qty', 'quantity', 'date', 'number', 'no', 'code', 'sku', 'description', 'weight', 'rate', 'tax', 'total']
    found_fields = Counter()
    
    # Analyze common terms for AI/Auto
    ai_terms = ['extract', 'ocr', 'validate', 'compare', 'comparison', 'match', 'classify', 'sort', 'email', 'merge', 'rename', 'scraping', 'lookup', 'predict', 'forecast']
    found_ai = Counter()
    
    # Analyze Sources/Targets
    system_terms = ['pdf', 'excel', 'email', 'sap', 'portal', 'web', 'sharepoint', 'drive', 'mailbox']
    found_systems = Counter()
    
    words = get_keywords(all_text)
    
    for word in words:
        if word in field_terms:
            found_fields[word] += 1
        if word in ai_terms:
            found_ai[word] += 1
        if word in system_terms:
            found_systems[word] += 1
            
    print("--- POTENTIAL SUB-ATTRIBUTES FREQUENCY ---")
    print(f"Fields: {found_fields.most_common()}")
    print(f"AI/Ops: {found_ai.most_common()}")
    print(f"Systems: {found_systems.most_common()}")

except Exception as e:
    print(f"Error: {e}")
