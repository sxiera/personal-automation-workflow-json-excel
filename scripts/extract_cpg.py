import pandas as pd
import json

input_file = '/Users/bimaaristo/MH/new/CPG-Research.xlsx'
output_file = '/Users/bimaaristo/MH/revise/cpg_data.json'

try:
    df = pd.read_excel(input_file)
    # Convert to json records
    data = df.to_dict(orient='records')
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully exported {len(data)} rows to {output_file}")
    
except Exception as e:
    print(f"Error extracting data: {e}")
