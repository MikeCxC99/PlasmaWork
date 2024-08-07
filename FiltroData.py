import pandas as pd

# Load the Excel file
file_path = 'F:\Codigos\datos_limpios.xlsx'
df = pd.read_excel(file_path)

# Keep the first row intact and filter the rest based on the condition in the 'K' column
filtered_df = df.iloc[1:][df['SYM/H (nT)'] <= -50]

# Concatenate the first row and the filtered rows
result_df = pd.concat([filtered_df])

# Save the result to a new Excel file
output_path = 'F:\Codigos\datos_filtrados.xlsx'
result_df.to_excel(output_path, index=False)
