## ¿Cuántos politologos se necesitan para codear un tracking electoral?
Este código sirve para llevar a cabo el seguimiento electoral de un candidato que utiliza datos sobre la imagen del candidato y la intención de voto de una muestra representativa de la población para analizar la evolución del apoyo a un candidato a lo largo del tiempo, con base en variables sociodemográficas y percepciones sobre la imagen del candidato. Implica:
- Limpieza y normalización de categorías de voto
- Cálculo de porcentajes diarios por candidato
- Rolling de días modificables
- Gráficos de los rolling
- Análisis estadísticos
- **Codificación de provincias para análisis estadísticos** (Nuevo!)

Extra: cada linea tiene al lado la explicacion de qué hace :)

## Instalación
Pasos para instalar o clonar el proyecto.
Clonar el repositorio:
Git bash
git clone https://github.com/usuario/nombre-del-proyecto.git
cd nombre-del-proyecto
pip install -r requirements.txt

## Librerías
-Pandas
-Numpy
-Seaborn
-Matplotlib

## Códigos de Provincia
El proyecto incluye un módulo para codificar provincias argentinas (ej: Córdoba = 04).
Ver [PROVINCIA_CODES_README.md](PROVINCIA_CODES_README.md) para más detalles.

Ejemplo de uso:
```python
from provincia_codes import provincia_to_code
codigo = provincia_to_code('Córdoba')  # Retorna '04'
```

Para ver ejemplos completos: `python3 ejemplo_provincia_codes.py`

## Autores
Chirichella, Franco
La Rosa Santoro, Mercedes 
Perlasca, Tomás
