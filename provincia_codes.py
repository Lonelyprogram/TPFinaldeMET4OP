"""
Módulo para manejar códigos de provincias argentinas
Este módulo proporciona funciones para convertir nombres de provincias a códigos numéricos y viceversa.
"""

# Diccionario de provincias argentinas con sus códigos oficiales
PROVINCIA_CODES = {
    'Buenos Aires': '01',
    'CABA': '02',  # Ciudad Autónoma de Buenos Aires
    'Catamarca': '03',
    'Córdoba': '04',
    'Corrientes': '05',
    'Entre Ríos': '06',
    'Jujuy': '07',
    'Mendoza': '08',
    'La Rioja': '09',
    'Salta': '10',
    'San Juan': '11',
    'San Luis': '12',
    'Santa Fe': '13',
    'Santiago del Estero': '14',
    'Tucumán': '15',
    'Chaco': '16',
    'Chubut': '17',
    'Formosa': '18',
    'Misiones': '19',
    'Neuquén': '20',
    'La Pampa': '21',
    'Río Negro': '22',
    'Santa Cruz': '23',
    'Tierra del Fuego': '24'
}

# Diccionario inverso para convertir códigos a nombres
CODE_TO_PROVINCIA = {v: k for k, v in PROVINCIA_CODES.items()}


def provincia_to_code(provincia_name):
    """
    Convierte el nombre de una provincia a su código numérico.
    
    Parámetros:
    -----------
    provincia_name : str
        Nombre de la provincia (puede estar en mayúsculas, minúsculas o mixto)
    
    Retorna:
    --------
    str : Código de dos dígitos de la provincia, o None si no se encuentra
    
    Ejemplos:
    ---------
    >>> provincia_to_code('Córdoba')
    '04'
    >>> provincia_to_code('cordoba')
    '04'
    >>> provincia_to_code('CÓRDOBA')
    '04'
    """
    # Validar entrada
    if provincia_name is None or not isinstance(provincia_name, str):
        return None
    
    # Manejar strings vacíos
    if not provincia_name.strip():
        return None
    
    # Normalizar el nombre (título case)
    normalized_name = provincia_name.strip().title()
    
    # Casos especiales para búsqueda flexible
    # Manejar variaciones comunes de nombres
    replacements = {
        'Cordoba': 'Córdoba',
        'Tucuman': 'Tucumán',
        'Entre Rios': 'Entre Ríos',
        'Neuquen': 'Neuquén',
        'Ciudad Autónoma De Buenos Aires': 'CABA',
        'Ciudad Autonoma De Buenos Aires': 'CABA',
        'Capital Federal': 'CABA',
        'Caba': 'CABA',  # Para cuando se pasa 'CABA' y se convierte a 'Caba'
    }
    
    for original, replacement in replacements.items():
        if normalized_name == original:
            normalized_name = replacement
            break
    
    return PROVINCIA_CODES.get(normalized_name)


def code_to_provincia(code):
    """
    Convierte un código numérico a nombre de provincia.
    
    Parámetros:
    -----------
    code : str o int
        Código de dos dígitos de la provincia
    
    Retorna:
    --------
    str : Nombre de la provincia, o None si no se encuentra
    
    Ejemplos:
    ---------
    >>> code_to_provincia('04')
    'Córdoba'
    >>> code_to_provincia(4)
    'Córdoba'
    >>> code_to_provincia('01')
    'Buenos Aires'
    """
    # Convertir a string y asegurar formato de 2 dígitos
    code_str = str(code).zfill(2)
    return CODE_TO_PROVINCIA.get(code_str)


def agregar_columna_codigo_provincia(df, columna_provincia='Provincia', columna_codigo='Codigo_Provincia'):
    """
    Agrega una columna con códigos de provincia a un DataFrame de pandas.
    
    NOTA: Esta función modifica el DataFrame en su lugar (in-place).
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con una columna de nombres de provincias
    columna_provincia : str, opcional
        Nombre de la columna que contiene los nombres de provincias (default: 'Provincia')
    columna_codigo : str, opcional
        Nombre de la nueva columna para los códigos (default: 'Codigo_Provincia')
    
    Retorna:
    --------
    pandas.DataFrame : DataFrame con la nueva columna de códigos (el mismo objeto modificado)
    
    Ejemplos:
    ---------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'Provincia': ['Córdoba', 'Buenos Aires', 'Santa Fe']})
    >>> df_con_codigos = agregar_columna_codigo_provincia(df)
    >>> print(df_con_codigos)
       Provincia Codigo_Provincia
    0    Córdoba               04
    1  Buenos Aires              01
    2    Santa Fe               13
    """
    df[columna_codigo] = df[columna_provincia].apply(provincia_to_code)
    return df


def listar_provincias_y_codigos():
    """
    Imprime una lista de todas las provincias y sus códigos.
    
    Retorna:
    --------
    None
    """
    print("Códigos de Provincias Argentinas:")
    print("-" * 40)
    for provincia, codigo in sorted(PROVINCIA_CODES.items(), key=lambda x: x[1]):
        print(f"{codigo} - {provincia}")


if __name__ == "__main__":
    # Ejemplos de uso
    print("=== Ejemplos de uso del módulo provincia_codes ===\n")
    
    # Listar todas las provincias y códigos
    listar_provincias_y_codigos()
    
    print("\n=== Ejemplos de conversión ===")
    # Ejemplo 1: Convertir nombre a código
    print(f"Córdoba -> {provincia_to_code('Córdoba')}")
    print(f"cordoba -> {provincia_to_code('cordoba')}")
    print(f"CÓRDOBA -> {provincia_to_code('CÓRDOBA')}")
    print(f"Buenos Aires -> {provincia_to_code('Buenos Aires')}")
    
    # Ejemplo 2: Convertir código a nombre
    print(f"\n04 -> {code_to_provincia('04')}")
    print(f"01 -> {code_to_provincia('01')}")
    print(f"13 -> {code_to_provincia('13')}")
    
    # Ejemplo 3: Uso con pandas
    print("\n=== Ejemplo con pandas DataFrame ===")
    import pandas as pd
    
    df_ejemplo = pd.DataFrame({
        'Provincia': ['Córdoba', 'Buenos Aires', 'Santa Fe', 'Mendoza', 'CABA']
    })
    
    df_con_codigos = agregar_columna_codigo_provincia(df_ejemplo)
    print(df_con_codigos)
