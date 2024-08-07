import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from datetime import timedelta, datetime

archivo_datos = 'F:\Codigos\datos_limpios.xlsx'
df = pd.read_excel(archivo_datos)

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

for column in columns_to_plot:
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=df_filtered['Datetime'], y=df_filtered[column], s=10)
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.title(f'{column} respecto al tiempo')

    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))
    plt.gcf().autofmt_xdate()

    plt.savefig('F:\Codigos\{column}_scatter_plot.png')
    plt.show()
