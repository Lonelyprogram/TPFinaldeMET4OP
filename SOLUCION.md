# Solución Implementada: Códigos de Provincia para Análisis Estadísticos

## Resumen

Se implementó un sistema completo de codificación de provincias argentinas para facilitar análisis estadísticos en el proyecto de tracking electoral.

## Problema Original

El usuario solicitó:
> "tengo la variable estrato que son provincias, como creo una forma de codigo para las mismas es decir cordoba = 01 para realizar un analisis estadisco"

**Traducción**: El usuario necesita un sistema para asignar códigos numéricos a las provincias argentinas (ejemplo: Córdoba = 04) para facilitar análisis estadísticos.

## Solución Implementada

### 1. Módulo Principal: `provincia_codes.py`

Contiene:
- **Diccionario completo** de las 24 provincias argentinas con códigos de 01 a 24
- **Funciones principales**:
  - `provincia_to_code(nombre)`: Convierte nombre de provincia a código
  - `code_to_provincia(codigo)`: Convierte código a nombre de provincia
  - `agregar_columna_codigo_provincia(df)`: Agrega columna de códigos a un DataFrame de pandas
  - `listar_provincias_y_codigos()`: Muestra todas las provincias y sus códigos

**Características especiales**:
- Manejo de mayúsculas/minúsculas (insensible a mayúsculas)
- Manejo de tildes/acentos (funciona con y sin tildes)
- Validación de entrada (maneja None, strings vacíos, tipos incorrectos)
- Soporte para variaciones de nombres (ej: "Capital Federal" = "CABA")

### 2. Documentación Completa: `PROVINCIA_CODES_README.md`

- Tabla completa de provincias y códigos
- Ejemplos de uso básico
- Ejemplos con pandas DataFrames
- Casos de uso para análisis estadísticos
- Ejemplos de visualización

### 3. Script de Ejemplos: `ejemplo_provincia_codes.py`

Demuestra:
- Conversión de nombres a códigos
- Conversión de códigos a nombres
- Uso en análisis estadístico (sin pandas)
- Agrupación por región
- Manejo de variaciones de nombres

### 4. Snippet para Notebooks: `snippet_para_notebooks.py`

Código listo para copiar y pegar en notebooks Jupyter que muestra:
- Cómo agregar códigos a DataFrames existentes
- Diferentes formas de integrar los códigos
- Ejemplos de análisis por provincia
- Ejemplos de visualización

### 5. Actualización del README Principal

Se agregó una sección sobre códigos de provincia con:
- Referencia a la documentación detallada
- Ejemplo de uso rápido
- Comando para ejecutar ejemplos

## Tabla de Códigos de Provincia

```
01 - Buenos Aires
02 - CABA (Ciudad Autónoma de Buenos Aires)
03 - Catamarca
04 - Córdoba
05 - Corrientes
06 - Entre Ríos
07 - Jujuy
08 - Mendoza
09 - La Rioja
10 - Salta
11 - San Juan
12 - San Luis
13 - Santa Fe
14 - Santiago del Estero
15 - Tucumán
16 - Chaco
17 - Chubut
18 - Formosa
19 - Misiones
20 - Neuquén
21 - La Pampa
22 - Río Negro
23 - Santa Cruz
24 - Tierra del Fuego
```

## Cómo Usar

### Uso Básico (sin pandas)

```python
from provincia_codes import provincia_to_code, code_to_provincia

# Obtener código de provincia
codigo = provincia_to_code('Córdoba')  # Retorna '04'

# Obtener nombre de provincia
nombre = code_to_provincia('04')  # Retorna 'Córdoba'
```

### Uso con Pandas DataFrames

```python
import pandas as pd
from provincia_codes import agregar_columna_codigo_provincia

# Cargar datos
df = pd.read_csv('data/encuesta100.csv')

# Opción 1: Si tienes una columna 'Provincia'
df = agregar_columna_codigo_provincia(df, columna_provincia='Provincia')

# Opción 2: Si tu 'Estrato' contiene provincias
df = agregar_columna_codigo_provincia(df, columna_provincia='Estrato', columna_codigo='Codigo_Provincia')

# Ahora puedes usar 'Codigo_Provincia' en tus análisis
```

### Ejemplo de Análisis Estadístico

```python
# Agrupar datos por provincia
resumen = df.groupby(['Codigo_Provincia', 'Provincia']).agg({
    'Voto': 'count',
    'Edad': 'mean',
    'Imagen del Candidato': 'mean'
})

# Ordenar por código de provincia
resumen_ordenado = resumen.sort_index()

# Filtrar por región (ejemplo: provincias 01-07)
df['Codigo_Num'] = df['Codigo_Provincia'].astype(int)
df_centro = df[df['Codigo_Num'] <= 7]
```

## Archivos Creados

1. `provincia_codes.py` - Módulo principal con las funciones
2. `PROVINCIA_CODES_README.md` - Documentación completa
3. `ejemplo_provincia_codes.py` - Script con ejemplos prácticos
4. `snippet_para_notebooks.py` - Código para integrar en notebooks
5. `.gitignore` - Para excluir archivos de build
6. `README.md` - Actualizado con referencia a la nueva funcionalidad
7. `SOLUCION.md` - Este archivo (resumen de la solución)

## Testing Realizado

✅ Todas las 24 provincias tienen códigos asignados
✅ Conversión bidireccional funciona correctamente
✅ Manejo de mayúsculas/minúsculas funciona
✅ Manejo de tildes/acentos funciona
✅ Validación de entrada (None, vacío, tipo incorrecto)
✅ Variaciones de CABA funcionan correctamente
✅ Sin vulnerabilidades de seguridad (CodeQL)
✅ Code review completado y issues corregidos

## Ventajas de Esta Solución

1. **Completa**: Incluye todas las 24 provincias argentinas
2. **Robusta**: Maneja diferentes formatos de entrada
3. **Documentada**: Documentación completa con ejemplos
4. **Probada**: Tests exhaustivos realizados
5. **Flexible**: Funciona con y sin pandas
6. **Educativa**: Ejemplos claros y código comentado
7. **Fácil de usar**: Interfaz simple y directa
8. **Segura**: Sin vulnerabilidades detectadas

## Próximos Pasos Sugeridos

Para integrar en tu análisis de tracking electoral:

1. Si tus datos tienen provincias en la columna "Estrato":
   ```python
   df = agregar_columna_codigo_provincia(df, columna_provincia='Estrato', columna_codigo='Codigo_Provincia')
   ```

2. Si necesitas agregar provincias a tus datos:
   ```python
   # Mapea tus estratos a provincias
   estratos_a_provincias = {
       'Alto': 'Buenos Aires',
       'Medio': 'Córdoba',
       'Bajo': 'Santa Fe'
   }
   df['Provincia'] = df['Estrato'].map(estratos_a_provincias)
   df = agregar_columna_codigo_provincia(df)
   ```

3. Usa los códigos en tus análisis:
   ```python
   # Análisis por provincia
   por_provincia = df.groupby('Codigo_Provincia')['Voto'].value_counts()
   
   # Visualizaciones
   df.groupby('Codigo_Provincia')['Imagen del Candidato'].mean().plot(kind='bar')
   ```

## Soporte

- Ver `PROVINCIA_CODES_README.md` para documentación detallada
- Ejecutar `python3 ejemplo_provincia_codes.py` para ver todos los ejemplos
- Consultar `snippet_para_notebooks.py` para código de integración
- El código está en `provincia_codes.py` con docstrings completos
