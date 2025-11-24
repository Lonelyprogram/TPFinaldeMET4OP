"""
Ejemplo de uso del módulo provincia_codes
Este script muestra cómo usar los códigos de provincia en análisis estadísticos
"""

# Si tienes pandas instalado, descomenta estas líneas:
# import pandas as pd
# from provincia_codes import provincia_to_code, code_to_provincia, agregar_columna_codigo_provincia, listar_provincias_y_codigos

# Para usar sin pandas, puedes usar las funciones básicas:
import sys
sys.path.append('.')  # Asegurar que el módulo esté en el path
from provincia_codes import provincia_to_code, code_to_provincia, listar_provincias_y_codigos, PROVINCIA_CODES

print("=" * 60)
print("EJEMPLOS DE USO DE CÓDIGOS DE PROVINCIA")
print("=" * 60)

# Ejemplo 1: Listar todas las provincias y sus códigos
print("\n1. LISTA COMPLETA DE PROVINCIAS Y CÓDIGOS:")
print("-" * 60)
listar_provincias_y_codigos()

# Ejemplo 2: Convertir nombres de provincia a códigos
print("\n2. CONVERTIR NOMBRES A CÓDIGOS:")
print("-" * 60)
provincias_ejemplo = ['Córdoba', 'Buenos Aires', 'Santa Fe', 'Mendoza', 'Tucumán', 'CABA']

for provincia in provincias_ejemplo:
    codigo = provincia_to_code(provincia)
    print(f"{provincia:25} -> Código: {codigo}")

# Ejemplo 3: Convertir códigos a nombres
print("\n3. CONVERTIR CÓDIGOS A NOMBRES:")
print("-" * 60)
codigos_ejemplo = ['01', '04', '13', '08', '15', '02']

for codigo in codigos_ejemplo:
    nombre = code_to_provincia(codigo)
    print(f"Código {codigo} -> {nombre}")

# Ejemplo 4: Manejo de variaciones en los nombres
print("\n4. MANEJO DE VARIACIONES EN LOS NOMBRES:")
print("-" * 60)
variaciones = [
    'cordoba',      # minúsculas
    'CÓRDOBA',      # mayúsculas
    'Córdoba',      # título
    'Cordoba',      # sin tilde
]

for variacion in variaciones:
    codigo = provincia_to_code(variacion)
    print(f"'{variacion:20}' -> Código: {codigo}")

# Ejemplo 5: Uso en análisis estadístico
print("\n5. EJEMPLO DE USO EN ANÁLISIS ESTADÍSTICO:")
print("-" * 60)
print("Supongamos que tienes datos de encuestas por provincia:\n")

# Datos de ejemplo (sin pandas)
datos_encuesta = [
    {'provincia': 'Córdoba', 'votos': 1500},
    {'provincia': 'Buenos Aires', 'votos': 3200},
    {'provincia': 'Santa Fe', 'votos': 1100},
    {'provincia': 'Mendoza', 'votos': 850},
]

print("Datos originales:")
for dato in datos_encuesta:
    print(f"  {dato['provincia']:20} - Votos: {dato['votos']}")

print("\nDatos con códigos de provincia:")
for dato in datos_encuesta:
    codigo = provincia_to_code(dato['provincia'])
    print(f"  Código {codigo} ({dato['provincia']:20}) - Votos: {dato['votos']}")

# Ejemplo 6: Crear un diccionario con códigos
print("\n6. DICCIONARIO DE DATOS CON CÓDIGOS:")
print("-" * 60)
datos_con_codigo = []
for dato in datos_encuesta:
    nuevo_dato = {
        'codigo_provincia': provincia_to_code(dato['provincia']),
        'provincia': dato['provincia'],
        'votos': dato['votos']
    }
    datos_con_codigo.append(nuevo_dato)

for dato in datos_con_codigo:
    print(f"  {dato}")

# Ejemplo 7: Agrupar por región (ejemplo)
print("\n7. EJEMPLO DE AGRUPACIÓN POR REGIÓN:")
print("-" * 60)
print("Códigos 01-07: Región Norte/Centro")
print("Códigos 08-15: Región Cuyo/NOA") 
print("Códigos 16-24: Región NEA/Patagonia")
print()

regiones = {
    'Norte/Centro': [],
    'Cuyo/NOA': [],
    'NEA/Patagonia': []
}

for dato in datos_con_codigo:
    codigo_num = int(dato['codigo_provincia'])
    if codigo_num <= 7:
        regiones['Norte/Centro'].append(dato)
    elif codigo_num <= 15:
        regiones['Cuyo/NOA'].append(dato)
    else:
        regiones['NEA/Patagonia'].append(dato)

for region, datos in regiones.items():
    total_votos = sum(d['votos'] for d in datos)
    print(f"{region}: {total_votos} votos totales")
    for d in datos:
        print(f"  - {d['provincia']} ({d['codigo_provincia']}): {d['votos']} votos")

print("\n" + "=" * 60)
print("Para usar con pandas DataFrames, ver el archivo provincia_codes.py")
print("Función: agregar_columna_codigo_provincia(df, columna_provincia, columna_codigo)")
print("=" * 60)
