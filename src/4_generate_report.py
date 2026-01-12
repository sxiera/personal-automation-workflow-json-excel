import pandas as pd
import json

input_json = './src/add-on.json'
output_excel = './src/final_assessment_result.xlsx'

try:
    # Load JSON
    with open(input_json, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        
        # Get the xlsxwriter workbook and worksheet objects.
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']
        
        # Add a text wrap format.
        wrap_format = workbook.add_format({'text_wrap': True, 'valign': 'top'})
        
        # Iterate through each column and set the width and format.
        for i, col in enumerate(df.columns):
            # Estimate width based on max content length, capped at 50 for readability
            # Calculate max length of data in this column
            max_len = 0
            # Check header length
            if len(str(col)) > max_len:
                max_len = len(str(col))
                
            # Check data length (sample first 100 rows to be fast if large, but here it is small)
            # Using astype(str) to handle potential NaNs or numbers
            column_len = df[col].astype(str).map(len).max()
            if column_len > max_len:
                max_len = column_len
            
            # Set width - minimum 10, maximum 50 (to prevent ultra wide columns), 
            # allowing wrap to handle the rest.
            final_width = max(10, min(max_len + 2, 60))
            
            worksheet.set_column(i, i, final_width, wrap_format)
            
    print(f"Successfully converted JSON to {output_excel}")
    print("Formatting applied: Text Wrapping enabled, Column Widths adjusted.")

except Exception as e:
    print(f"Error converting to Excel: {e}")
