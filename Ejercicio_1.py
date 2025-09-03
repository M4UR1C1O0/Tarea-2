# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacioón del DataFrame
df_alumnos = pd.DataFrame(datos)

# Cálculo del promedio de las notas