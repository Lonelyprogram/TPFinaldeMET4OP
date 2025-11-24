"""
Código para agregar a los notebooks de análisis electoral
Este snippet muestra cómo integrar los códigos de provincia en tu análisis
"""

# ==============================================================================
# SECCIÓN: CODIFICACIÓN DE PROVINCIAS
# ==============================================================================
# Este código muestra cómo agregar códigos de provincia a tus datos de encuesta
# para facilitar análisis estadísticos por región geográfica.

# Importar pandas y las funciones necesarias
import pandas as pd

from provincia_codes import (
    provincia_to_code, 
    code_to_provincia, 
    agregar_columna_codigo_provincia,
    listar_provincias_y_codigos
)

# ------------------------------------------------------------------------------
# Opción 1: Si tu DataFrame tiene una columna con nombres de provincias
# ------------------------------------------------------------------------------
# Ejemplo: Si tienes una columna llamada 'Provincia' o si 'Estrato' contiene provincias

# Agregar columna de códigos al DataFrame
df = agregar_columna_codigo_provincia(
    df, 
    columna_provincia='Provincia',  # Cambia esto al nombre de tu columna
    columna_codigo='Codigo_Provincia'
)

# Verificar el resultado
print(df[['Provincia', 'Codigo_Provincia']].head())

# ------------------------------------------------------------------------------
# Opción 2: Convertir valores individuales
# ------------------------------------------------------------------------------
# Si necesitas convertir nombres de provincia a códigos uno por uno

provincia = 'Córdoba'
codigo = provincia_to_code(provincia)
print(f"{provincia} -> Código: {codigo}")

# O convertir código a nombre
codigo = '04'
nombre = code_to_provincia(codigo)
print(f"Código {codigo} -> {nombre}")

# ------------------------------------------------------------------------------
# Opción 3: Agregar provincia manualmente a cada fila
# ------------------------------------------------------------------------------
# Si tu DataFrame no tiene provincias pero quieres agregarlas

# Crear una columna de provincia (ejemplo: asignar Córdoba a todas las filas)
df['Provincia'] = 'Córdoba'

# Luego agregar los códigos
df['Codigo_Provincia'] = df['Provincia'].apply(provincia_to_code)

# ------------------------------------------------------------------------------
# Opción 4: Mapear desde otra variable (ej: Estrato -> Provincia)
# ------------------------------------------------------------------------------
# Si tienes estratos que corresponden a provincias, crea un mapeo

# Ejemplo de mapeo de estrato a provincia
estrato_a_provincia = {
    'Alto': 'Buenos Aires',
    'Medio': 'Córdoba',
    'Bajo': 'Santa Fe'
}

# Aplicar el mapeo
df['Provincia'] = df['Estrato'].map(estrato_a_provincia)
df['Codigo_Provincia'] = df['Provincia'].apply(provincia_to_code)

# ------------------------------------------------------------------------------
# Análisis por Provincia
# ------------------------------------------------------------------------------

# Contar votos por provincia
votos_por_provincia = df.groupby(['Codigo_Provincia', 'Provincia'])['Voto'].value_counts()
print("\nDistribución de votos por provincia:")
print(votos_por_provincia)

# Estadísticas por provincia
stats_provincia = df.groupby(['Codigo_Provincia', 'Provincia']).agg({
    'Edad': ['mean', 'median'],
    'Imagen del Candidato': 'mean',
    'Voto': 'count'
})
print("\nEstadísticas por provincia:")
print(stats_provincia)

# Agrupar por región usando los códigos
# (ejemplo: códigos 01-10 = Centro, 11-20 = Interior, 21-24 = Patagonia)
df['Codigo_Num'] = df['Codigo_Provincia'].astype(int)
df['Region'] = pd.cut(
    df['Codigo_Num'], 
    bins=[0, 10, 20, 24], 
    labels=['Centro', 'Interior', 'Patagonia']
)

region_stats = df.groupby('Region')['Voto'].value_counts()
print("\nDistribución de votos por región:")
print(region_stats)

# ------------------------------------------------------------------------------
# Visualización
# ------------------------------------------------------------------------------

# Gráfico de votos por provincia (requiere matplotlib)
import matplotlib.pyplot as plt

votos_por_prov = df.groupby('Codigo_Provincia')['Voto'].value_counts().unstack(fill_value=0)
votos_por_prov.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Distribución de Votos por Código de Provincia')
plt.xlabel('Código de Provincia')
plt.ylabel('Cantidad de Votos')
plt.legend(title='Candidato', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# Exportar datos con códigos de provincia
# ------------------------------------------------------------------------------

# Guardar el DataFrame con los códigos agregados
df.to_csv('datos_con_codigos_provincia.csv', index=False)
print("\nDatos guardados en 'datos_con_codigos_provincia.csv'")

# ------------------------------------------------------------------------------
# Ver lista completa de provincias y códigos
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print("LISTA COMPLETA DE PROVINCIAS Y CÓDIGOS")
print("="*60)
listar_provincias_y_codigos()
