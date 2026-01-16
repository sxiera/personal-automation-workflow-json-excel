import pandas as pd

input_file = '/Users/bimaaristo/MH/revise/add-on-v2.xlsx'

try:
    xl = pd.ExcelFile(input_file)
    print(f"Sheet names: {xl.sheet_names}")
    
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        print(f"Sheet '{sheet}': {len(df)} rows")
        
except Exception as e:
    print(f"Error inspecting file: {e}")
