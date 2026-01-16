import pandas as pd
import json
import os

input_file = './data/misc/add-on.xlsx'
output_file = './data/misc/add-on.json'

try:
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        exit(1)

    df = pd.read_excel(input_file)
    print("Columns found:", df.columns.tolist())
    
    # Convert to list of dictionaries
    data = df.to_dict(orient='records')
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4, default=str)
        
    print(f"Successfully converted {input_file} to {output_file}")
    
except Exception as e:
    print(f"Error converting file: {e}")
