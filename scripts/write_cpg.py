import pandas as pd
import json

input_file = '/Users/bimaaristo/MH/revise/cpg_rewritten.json'
output_file = '/Users/bimaaristo/MH/new/CPG-Research-Rewritten.xlsx'

try:
    with open(input_file, 'r') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    
    # Ensure column order matches original mostly
    columns = ['No', 'Key Topics', 'Client', 'Business Case and Page Info', 'Source', 'Relevancy']
    # Filter for columns that actually exist in the data keys just in case
    columns = [c for c in columns if c in df.columns]
    
    df = df[columns]
    
    df.to_excel(output_file, index=False)
        
    print(f"Successfully wrote {len(df)} rows to {output_file}")
    
except Exception as e:
    print(f"Error writing excel: {e}")
