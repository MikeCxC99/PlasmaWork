import pandas as pd
import matplotlib.pyplot as plt

input_excel_file = 'cooked_data.xlsx'
df = pd.read_excel(input_excel_file)

instances = df['Data_instance']
values_columns = df.loc[:, 'Value_1':'Value_22'] 

plt.figure(figsize=(12, 8))

for idx, row in df.iterrows():
    plt.plot(values_columns.columns, row['Value_1':'Value_22'], label=f'Instance {row["Data_instance"]}')

plt.title('Value_N vs Instancia')
plt.xlabel('Value_N')
plt.ylabel('Valor')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), ncol=1)
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
