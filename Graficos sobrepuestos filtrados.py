import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from datetime import timedelta, datetime

file_path_with_headers = 'F:\Codigos\datos_filtrados.xlsx'
df = pd.read_excel(file_path_with_headers)

columns_to_plot = [
    "Field magnitude average (nT)", 
    "Speed (km/s)", 
    "Proton Density (n/cc)", 
    "Proton Temperature (K)", 
    "Flow pressure (nPa)", 
    "Plasma beta", 
    "SYM/H (nT)"
]

def convert_to_datetime(row):
    base_date = datetime(2024, 1, 1)
    day_of_year = int(row['Dia del año'])
    hour = int(row['Hora'])
    minute = int(row['Minuto'])
    return base_date + timedelta(days=day_of_year - 1, hours=hour, minutes=minute)

df['Datetime'] = df.apply(convert_to_datetime, axis=1)

df_filtered = df[(df['Dia del año'] >= 131) & (df['Dia del año'] <= 136)]

plt.figure(figsize=(12, 6))
for column in columns_to_plot:
    sns.scatterplot(x=df_filtered['Datetime'], y=df_filtered[column], s=10, label=column)

plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.title('Todos los parametros respecto al tiempo')
plt.legend()

plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_minor_locator(mdates.HourLocator(interval=6))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
plt.gcf().autofmt_xdate()

plt.savefig('F:\Codigos\overlapped_scatter_plot.png')
plt.show()
