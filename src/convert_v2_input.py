import pandas as pd
import json
import os

input_file = '/Users/bimaaristo/MH/revise/add-on-v2.xlsx'
output_file = '/Users/bimaaristo/MH/revise/add-on-v2.json'

try:
    # Read specific sheet 'Use Cases'
    df = pd.read_excel(input_file, sheet_name='Use Cases')
    print("Columns found:", df.columns.tolist())
    
    data = df.to_dict(orient='records')
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4, default=str)
        
    print(f"Successfully converted sheet 'Use Cases' to {output_file}")
    print(f"Total records: {len(data)}")
    
except Exception as e:
    print(f"Error converting file: {e}")
