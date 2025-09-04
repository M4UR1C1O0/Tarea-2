# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacioón del DataFrame
df_alumnos = pd.DataFrame(datos)

df_alumnos['Promedio'] = round(df_alumnos[['Nota1', 'Nota2', 'Nota3']].mean(axis=1),1)

df_ordenado_descendente = df_alumnos.sort_values(by= 'Promedio',ascending=False).reset_index(drop=True)

print("Listado Ordenado de forma Descendente de los promedios del curso",df_ordenado_descendente)
