# Códigos de Provincia para Análisis Estadísticos

Este documento explica cómo usar los códigos de provincia en tus análisis estadísticos del tracking electoral.

## ¿Qué es esto?

El módulo `provincia_codes.py` proporciona funciones para convertir nombres de provincias argentinas a códigos numéricos (como Córdoba = 04) y viceversa. Esto es útil para análisis estadísticos, agrupaciones, y codificación de datos.

## Códigos de Provincias Argentinas

| Código | Provincia |
|--------|-----------|
| 01 | Buenos Aires |
| 02 | CABA (Ciudad Autónoma de Buenos Aires) |
| 03 | Catamarca |
| 04 | Córdoba |
| 05 | Corrientes |
| 06 | Entre Ríos |
| 07 | Jujuy |
| 08 | Mendoza |
| 09 | La Rioja |
| 10 | Salta |
| 11 | San Juan |
| 12 | San Luis |
| 13 | Santa Fe |
| 14 | Santiago del Estero |
| 15 | Tucumán |
| 16 | Chaco |
| 17 | Chubut |
| 18 | Formosa |
| 19 | Misiones |
| 20 | Neuquén |
| 21 | La Pampa |
| 22 | Río Negro |
| 23 | Santa Cruz |
| 24 | Tierra del Fuego |

## Instalación

No requiere instalación adicional. Solo necesitas tener Python 3.x instalado.

## Uso Básico

### 1. Importar el módulo

```python
from provincia_codes import provincia_to_code, code_to_provincia, listar_provincias_y_codigos
```

### 2. Convertir nombre de provincia a código

```python
codigo = provincia_to_code('Córdoba')
print(codigo)  # Output: '04'

codigo = provincia_to_code('Buenos Aires')
print(codigo)  # Output: '01'
```

El módulo maneja diferentes formatos:
```python
provincia_to_code('CÓRDOBA')   # '04'
provincia_to_code('córdoba')   # '04'
provincia_to_code('Cordoba')   # '04' (sin tilde también funciona)
```

### 3. Convertir código a nombre de provincia

```python
nombre = code_to_provincia('04')
print(nombre)  # Output: 'Córdoba'

nombre = code_to_provincia(1)  # También acepta números
print(nombre)  # Output: 'Buenos Aires'
```

### 4. Listar todas las provincias y códigos

```python
listar_provincias_y_codigos()
```

## Uso con Pandas DataFrames

Si tienes pandas instalado, puedes usar la función `agregar_columna_codigo_provincia`:

```python
import pandas as pd
from provincia_codes import agregar_columna_codigo_provincia

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Provincia': ['Córdoba', 'Buenos Aires', 'Santa Fe', 'Mendoza']
})

# Agregar columna de códigos
df = agregar_columna_codigo_provincia(df, columna_provincia='Provincia', columna_codigo='Codigo')

print(df)
#        Provincia Codigo
# 0       Córdoba     04
# 1  Buenos Aires     01
# 2     Santa Fe     13
# 3       Mendoza     08
```

## Ejemplos de Uso en Análisis Estadísticos

### Ejemplo 1: Agrupar datos por código de provincia

```python
import pandas as pd
from provincia_codes import agregar_columna_codigo_provincia

# Datos de encuesta
df = pd.DataFrame({
    'Provincia': ['Córdoba', 'Buenos Aires', 'Córdoba', 'Santa Fe', 'Buenos Aires'],
    'Votos': [150, 320, 180, 110, 290]
})

# Agregar códigos
df = agregar_columna_codigo_provincia(df)

# Agrupar por código de provincia
resumen = df.groupby('Codigo_Provincia')['Votos'].sum()
print(resumen)
```

### Ejemplo 2: Ordenar por código de provincia

```python
# Ordenar datos por código de provincia
df_ordenado = df.sort_values('Codigo_Provincia')
print(df_ordenado)
```

### Ejemplo 3: Filtrar por región usando códigos

```python
# Filtrar provincias de la región Norte (códigos 01-07)
df['Codigo_Num'] = df['Codigo_Provincia'].astype(int)
df_norte = df[df['Codigo_Num'] <= 7]
```

## Integración con tu Proyecto de Tracking Electoral

Para usar estos códigos en tu análisis de tracking electoral:

1. **Si tu variable "Estrato" representa provincias:**
   ```python
   import pandas as pd
   from provincia_codes import agregar_columna_codigo_provincia
   
   # Cargar tus datos
   df = pd.read_csv('data/encuesta100.csv')
   
   # Si "Estrato" contiene nombres de provincias
   df = agregar_columna_codigo_provincia(df, columna_provincia='Estrato', columna_codigo='Codigo_Provincia')
   
   # Ahora puedes usar 'Codigo_Provincia' en tus análisis
   ```

2. **Si quieres agregar una nueva columna de provincias:**
   ```python
   # Agregar una columna de provincia a tus datos
   df['Provincia'] = 'Córdoba'  # o cargarla de otra fuente
   df = agregar_columna_codigo_provincia(df)
   ```

## Ejemplos Prácticos

### Crear gráficos agrupados por código de provincia

```python
import pandas as pd
import matplotlib.pyplot as plt
from provincia_codes import agregar_columna_codigo_provincia

# Cargar y preparar datos
df = pd.read_csv('data/encuesta100.csv')
# Asumiendo que tienes una columna 'Provincia'
df = agregar_columna_codigo_provincia(df)

# Agrupar votos por provincia
votos_por_provincia = df.groupby(['Codigo_Provincia', 'Provincia'])['Voto'].value_counts().unstack()

# Crear gráfico
votos_por_provincia.plot(kind='bar', stacked=True)
plt.title('Distribución de Votos por Provincia')
plt.xlabel('Código de Provincia')
plt.ylabel('Cantidad de Votos')
plt.legend(title='Candidato')
plt.tight_layout()
plt.show()
```

### Análisis estadístico por provincia

```python
import pandas as pd
from provincia_codes import agregar_columna_codigo_provincia

# Cargar datos
df = pd.read_csv('data/encuesta100.csv')
df = agregar_columna_codigo_provincia(df)

# Estadísticas descriptivas por provincia
stats_por_provincia = df.groupby('Codigo_Provincia').agg({
    'Edad': ['mean', 'median', 'std'],
    'Imagen del Candidato': ['mean', 'std'],
    'Voto': 'count'
})

print(stats_por_provincia)
```

## Ejecutar Ejemplos

Para ver todos los ejemplos en acción:

```bash
python3 ejemplo_provincia_codes.py
```

## Funciones Disponibles

### `provincia_to_code(provincia_name)`
Convierte nombre de provincia a código.
- **Parámetro**: `provincia_name` (str) - Nombre de la provincia
- **Retorna**: Código de dos dígitos (str) o None si no se encuentra

### `code_to_provincia(code)`
Convierte código a nombre de provincia.
- **Parámetro**: `code` (str o int) - Código de la provincia
- **Retorna**: Nombre de la provincia (str) o None si no se encuentra

### `agregar_columna_codigo_provincia(df, columna_provincia='Provincia', columna_codigo='Codigo_Provincia')`
Agrega una columna con códigos a un DataFrame.
- **Parámetros**: 
  - `df` (DataFrame) - DataFrame con columna de provincias
  - `columna_provincia` (str) - Nombre de la columna con provincias
  - `columna_codigo` (str) - Nombre para la nueva columna de códigos
- **Retorna**: DataFrame con la nueva columna

### `listar_provincias_y_codigos()`
Imprime la lista completa de provincias y códigos.

## Notas

- Los códigos están basados en una numeración estándar de las provincias argentinas
- El módulo maneja variaciones en la escritura (mayúsculas, minúsculas, con/sin tildes)
- CABA y Capital Federal se reconocen como sinónimos

## Soporte

Para más información, consulta el código fuente en `provincia_codes.py` o el ejemplo completo en `ejemplo_provincia_codes.py`.
