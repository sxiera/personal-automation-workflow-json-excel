import pandas as pd
import json
import datetime

input_file = '/Users/bimaaristo/MH/newest/CPG-Research (1).xlsx'
output_file = '/Users/bimaaristo/MH/revise/cpg_newest.json'

def default_converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    return str(o)

try:
    # Read with header=1 to capture the correct column names
    df = pd.read_excel(input_file, header=1)
    
    # Fill NaN with empty string
    df = df.fillna("")
    
    # Convert to json records
    data = df.to_dict(orient='records')
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2, default=default_converter)
        
    print(f"Successfully exported {len(data)} rows to {output_file}")
    
except Exception as e:
    print(f"Error extracting data: {e}")
