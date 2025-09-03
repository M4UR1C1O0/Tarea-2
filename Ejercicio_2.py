# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacioón del DataFrame
df_alumnos = pd.DataFrame(datos)

# Cuantos aprobaron con mayor a 4.0

# Guardamos los aprobados en una nueva variable
df_alumnos_aprobados = df_alumnos[df_alumnos['Promedio'] > 4.0]

print(df_alumnos_aprobados)