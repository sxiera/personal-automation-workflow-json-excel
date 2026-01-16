import json
import re

def clean_key_topics(text):
    if not isinstance(text, str):
        return ""
    
    # Remove initial artifacts
    text = text.replace("—\t\n", "").strip()
    
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Filter out common metadata lines that clutter the topic
    filtered_lines = []
    metadata_keywords = [
        "Non Applicable", 
        "Brands (Automative, Cpg)", 
        "Brands (Automotive, Cpg)", 
        "Retail (Retail, E-Commerce)",
        "Luxury",
        "Marketing", 
        "Sales", 
        "Office Operations",
        "Data/Ai Strategy",
        "Ai Transformation",
        "Data Governance & Management",
        "Insights",
        "Asset",
        "Client Pitch", 
        "One Pager", 
        "Offer", 
        "Client Document",
        "End Of Project",
        "—"
    ]
    
    doc_type = ""
    
    for line in lines:
        is_metadata = False
        # check if line is purely a known metadata keyword
        if line in metadata_keywords:
            is_metadata = True
            # We might want to capture doc type if we see it
            if line in ["Client Pitch", "One Pager", "Offer", "Client Document", "End Of Project", "Insights", "Asset"]:
                doc_type = line
        
        if not is_metadata:
            filtered_lines.append(line)
            
    # Join meaningful lines. If the result is short, just return it.
    description = ". ".join(filtered_lines)
    
    if doc_type:
        description = f"[{doc_type}] {description}"
        
    return description

def clean_client(text):
    if not isinstance(text, str) or text == "-":
        return text
    
    # Standardize names
    text = text.replace("Lvmh (Group)", "LVMH Group")
    text = text.replace("L'oréal", "L'Oréal")
    text = text.replace("L'oreal", "L'Oréal")
    text = text.replace("Ab Inbev", "AB InBev")
    
    return text.title() if text.isupper() else text

def clean_business_case(text):
    if not isinstance(text, str):
        return "-"
    
    if text in ["NaN", "Non Applicable", "Doesnt Exist", "Not relevant", "Not relevant, just a treasure data implementation", "Not relevant (docs only)"]:
        return "-"
        
    # Formatting bullet points if simpler
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("- "):
            cleaned_lines.append(line)
        elif line.startswith("Page:"):
             cleaned_lines.append("Page References:")
        elif line:
             cleaned_lines.append(line)
             
    return "\n".join(cleaned_lines)

input_file = '/Users/bimaaristo/MH/revise/cpg_data.json'
output_file = '/Users/bimaaristo/MH/revise/cpg_rewritten.json'

try:
    with open(input_file, 'r') as f:
        data = json.load(f)

    processed_data = []
    for item in data:
        new_item = item.copy()
        new_item['Key Topics'] = clean_key_topics(item.get('Key Topics', ''))
        new_item['Client'] = clean_client(item.get('Client', ''))
        new_item['Business Case and Page Info'] = clean_business_case(item.get('Business Case and Page Info', ''))
        processed_data.append(new_item)

    with open(output_file, 'w') as f:
        json.dump(processed_data, f, indent=2)
        
    print(f"Successfully processed {len(processed_data)} items to {output_file}")

except Exception as e:
    print(f"Error processing data: {e}")
