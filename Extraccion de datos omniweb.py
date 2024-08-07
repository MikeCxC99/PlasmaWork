import pandas as pd

ruta_archivo = 'F:\Codigos\omni_min_OJPfu3z5IG.lst'

with open(ruta_archivo, 'r') as file:
    lines = file.readlines()

datos_limpios = []
for line in lines:
    row = line.strip().split()
    if not any(data.startswith('999') for data in row):
        datos_limpios.append(row)

headers = ["Año", "Dia del año", "Hora", "Minuto", "Field magnitude average (nT)", 
           "Speed (km/s)", "Proton Density (n/cc)", "Proton Temperature (K)", 
           "Flow pressure (nPa)", "Plasma beta", "SYM/H (nT)"]

df = pd.DataFrame(datos_limpios, columns=headers)

archivo_salida = 'F:\Codigos\datos_limpios.xlsx'
df.to_excel(archivo_salida, index=False, header=True)

archivo_salida
