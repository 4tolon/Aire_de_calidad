# Aire de calidad

Un análisis temporal de la calidad del aire de la ciudad y la comunidada de Madrid.

https://public.tableau.com/app/profile/fernando6962/viz/deMadrid/PresesntacionFinal


![portada](https://www.diyphotography.net/wp-content/uploads/2016/11/timelapse_zoom.gif)
![](/img/Dashboard.png)

# Objetivo
El objetivo del proyecto ha sido la creación de una presentacion original  en Tableau, la manipulacion de grandes volumenes de datos y archivos mediante codigo Python, a través de funciones creadas en **scr/funciones.py** y de numerosos cuadernos de Jupyter Notebooks manejados con Jupyter Lab. 

### Dashboad final:

En este dash board se puede selecionar la estacion de medidad que quieras del ayuntamiento o de la comunidad de Madrid. Mediante un filto a la serie temporal se piede limitar la informacion mostrada en cada gráfica a un rango de tiempo concreto de los últimos seis años. Toda la información mostrada se ajusta a ese rango.

![](/img/dash1.png)

### Descripción:

**Parte central** 
- Estacion de medida: Selección de la estacion de medida por código-
- Rango de fechas de cálculo. Selección mediante introducción directa de fechas o deslizantes.
- Mapa: localización de la estación selecionada.
- Ensayos de calidad de arie en esa estación.

**Panel derecho** 
- Gráficas de la serie tempotal, de cada ensayo, seleccionada en la estación correspondiente.
- Boxplots de los ensayo que muestra la distribución de los valores de cada ensayo.

**Panel izquierdo**
- Círculos que muestran el promedio de valores para cada ensayo.
- Gráfica de barras anidada para ver la distribucion general de valores de cada ensayo.

 
# Working plan 

![workingflow](https://borealtelevision.com/wp-content/uploads/2021/06/NUBES.gif)

Descarga de datos en el portal de datos abiertos de la comunidad  y el ayuntamiento de **Madrid**. 


Coordinación de los archivos optenidos mediane manipulacion con **Pandas** 

EDA; análisis explorarorio de los datos unificados. 

Ensayos con difenrentes tipos de tecnologias de visualización, desde el propio pandas, pasando por seaborn y matplotlib, folium o kepler.

Determinación de no implemetar la idea de mostrar los datos como si fueran estratos geológicos en prefiles selcionados que atravesasen la comundad de Madrid. La alta variabilidad de los datos de una hora a la siguiente me hacen desistir de la idea. No hay una constancia ni estabilidad que propicien la creacion de perfiles de contaminates. 

Selección de Tableau como herramienta de visualización para mostrar los datos manipulados.

Creación de los Dashboards.

Presentación del proyecto.

# Estructura 

El repositorio está formado diferenetes carpetas:

1. **notebooks**: 
    
    Numerosos cuadernos para crear las funciones y manipular a los archivos, crearlos, y almacenarlos.

    Exploracion preliminar de los datos. 

2. **scr** :   
    
    **Cargadata.py** Archivo de funciones para la manipulación de dataframes de Pandas.

3. **Data**:

    Almacén de los diversos tipos de datos utilizados en el proyecto, carpeta temporal de tranformación de archivos.

4. **img**: 
    
    Almacén de inagenes, figuras y gráficos.

5. **kepler**: 

    Desarroyo de mapas mediante kelper (finalmente no usado en presentación final)    

# Libraries

[sys](https://docs.python.org/3/library/sys.html)

[glob](https://docs.python.org/es/3/library/glob.html)

[pandas](https://pandas.pydata.org/)

[tablau](https://public.tableau.com)

[json](https://docs.python.org/3/library/json.html)

[os](https://docs.python.org/3/library/os.html)

[geopandas](https://geopandas.org/)

[kepler gl](https://kepler.gl/)

[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)

