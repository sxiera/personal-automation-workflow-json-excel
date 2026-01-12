import json

file_path = './src/add-on.json'
try:
    with open(file_path, 'r') as f:
        data = json.load(f)

    print(f"--- Scanning {len(data)} Items for Context Audit ---\n")
    
    for idx, item in enumerate(data):
        print(f"ID: {idx} | Topic: {item.get('Topic', 'N/A')}")
        print(f"CONTEXT: {item.get('Description', '')} | {item.get('Remarks', '')}")
        print(f"   -> Source: {item.get('Source System', '')}")
        print(f"   -> Target: {item.get('Target System', '')}")
        print(f"   -> Extract: {item.get('Field Extraction', '').replace(chr(10), '; ')}")
        print(f"   -> Result: {item.get('Expected Final Result', '').replace(chr(10), '; ')}")
        print(f"   -> AI/Auto: {item.get('Automation / AI Capabilities', '').replace(chr(10), '; ')}")
        print("-" * 60)

except Exception as e:
    print(f"Error: {e}")
