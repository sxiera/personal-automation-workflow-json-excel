import pandas as pd

input_file = '/Users/bimaaristo/MH/new/CPG-Research.xlsx'

try:
    xl = pd.ExcelFile(input_file)
    print(f"Sheet names: {xl.sheet_names}")
    
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        print(f"\nSheet: '{sheet}'")
        print(f"Columns: {list(df.columns)}")
        print("First 3 rows:")
        print(df.head(3).to_string())
        
except Exception as e:
    print(f"Error inspecting file: {e}")
