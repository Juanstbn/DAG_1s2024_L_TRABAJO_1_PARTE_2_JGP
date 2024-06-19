## Instalación

Para ejecutar este proyecto, sigue los siguientes pasos:

1. **Requisitos previos**:
   - Debes tener instalado ArcGIS Pro en tu computadora.
   
2. **Pasos**:
   1. Clona este repositorio en tu máquina local:
      ```bash
      git clone https://github.com/tu-usuario/nombre-repositorio.git
      ```
   2. Abre ArcGIS Pro y carga los archivos de proyecto del repositorio clonado.
   3. Sigue las instrucciones específicas de cada código para ejecutar las diferentes etapas del análisis.

## Uso

El proyecto está compuesto por varios scripts independientes que se ejecutan secuencialmente para alcanzar el análisis final. Cada script tiene un propósito específico:

### `create_buffer.py`

Este script genera una zona de influencia (buffer) de 400 metros alrededor de las áreas verdes especificadas en la comuna de La Cisterna.

- **Parámetros de Entrada**:
  - `fcIn`: La capa de entrada que contiene las áreas verdes.
  - `dirOut`: El directorio de salida donde se almacenará el resultado.
  - `nameOut`: El nombre del archivo resultante que contendrá la zona de influencia.

- **Uso**:
  1. Abre ArcGIS Pro y asegura que el proyecto actual está cargado.
  2. Corre el script con los parámetros necesarios. Ejemplo en Python:
     ```python
     import arcpy

     def script_tool(fcIn, dirOut, nameOut):
         return

     if __name__ == "__main__":
         fcIn = arcpy.GetParameterAsText(0)  # Areas verdes
         dirOut = arcpy.GetParameterAsText(1) # Directorio salida
         nameOut = arcpy.GetParameterAsText(2) # Nombre de la zona de influencia (buffer)

         script_tool(fcIn, dirOut, nameOut)
         arcpy.SetParameterAsText(2, "Result")

     # DEFINIR ENTORNO
     aprx = arcpy.mp.ArcGISProject("CURRENT")
     aprxMap = aprx.listMaps()[0]
     arcpy.AddMessage("Se iniciaron los parámetros de entrada")

     # AGREGAR CAPAS DE CONTENIDO
     aprxMap.addDataFromPath(fcIn)
     content = []
     content.append(aprxMap.listLayers()[0].name)

     # GEO PROCESO
     fcOut = f"{dirOut}\{str(nameOut)}" # Ruta completa del archivo de salida
     dist = "400"  # Estándar recomendado por INE
     distBuffer = f"{dist} Meters"
     
     arcpy.analysis.Buffer(fcIn, fcOut, distBuffer, "FULL", "ROUND", "ALL", None, "PLANAR")
     arcpy.AddMessage("Geo proceso terminado")

     # AGREGAR RESULTADO A LA TABLA DE CONTENIDO
     aprxMap.addDataFromPath(fcOut)
     ```

- **Resultado**: El script crea un archivo de salida que contiene la zona de influencia alrededor de las áreas verdes y lo añade al proyecto de ArcGIS Pro.
paso 2
## Instalación

Para ejecutar este proyecto, sigue los siguientes pasos:

1. **Requisitos previos**:
   - Debes tener instalado ArcGIS Pro en tu computadora.
   
2. **Pasos**:
   1. Clona este repositorio en tu máquina local:
      ```bash
      git clone https://github.com/tu-usuario/nombre-repositorio.git
      ```
   2. Abre ArcGIS Pro y carga los archivos de proyecto del repositorio clonado.
   3. Sigue las instrucciones específicas de cada código para ejecutar las diferentes etapas del análisis.

## Uso

El proyecto está compuesto por varios scripts independientes que se ejecutan secuencialmente para alcanzar el análisis final. Cada script tiene un propósito específico:

### `create_buffer.py`

Este script genera una zona de influencia (buffer) de 400 metros alrededor de las áreas verdes especificadas en la comuna de La Cisterna.

- **Parámetros de Entrada**:
  - `fcIn`: La capa de entrada que contiene las áreas verdes.
  - `dirOut`: El directorio de salida donde se almacenará el resultado.
  - `nameOut`: El nombre del archivo resultante que contendrá la zona de influencia.

- **Uso**:
  1. Abre ArcGIS Pro y asegúrate de que el proyecto actual está cargado.
  2. Corre el script con los parámetros necesarios. Ejemplo en Python:
     ```python
     import arcpy

     def script_tool(fcIn, dirOut, nameOut):
         return

     if __name__ == "__main__":
         fcIn = arcpy.GetParameterAsText(0)  # Áreas verdes
         dirOut = arcpy.GetParameterAsText(1) # Directorio de salida
         nameOut = arcpy.GetParameterAsText(2) # Nombre de la zona de influencia (buffer)

         script_tool(fcIn, dirOut, nameOut)
         arcpy.SetParameterAsText(2, "Result")

     # DEFINIR ENTORNO
     aprx = arcpy.mp.ArcGISProject("CURRENT")
     aprxMap = aprx.listMaps()[0]
     arcpy.AddMessage("Se iniciaron los parámetros de entrada")

     # AGREGAR CAPAS DE CONTENIDO
     aprxMap.addDataFromPath(fcIn)
     content = []
     content.append(aprxMap.listLayers()[0].name)

     # GEO PROCESO
     fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida
     dist = "400"  # Estándar recomendado por INE
     distBuffer = f"{dist} Meters"
     
     arcpy.analysis.Buffer(fcIn, fcOut, distBuffer, "FULL", "ROUND", "ALL", None, "PLANAR")
     arcpy.AddMessage("Geo proceso terminado")

     # AGREGAR RESULTADO A LA TABLA DE CONTENIDO
     aprxMap.addDataFromPath(fcOut)
     ```

- **Resultado**: El script crea un archivo de salida que contiene la zona de influencia alrededor de las áreas verdes y lo añade al proyecto de ArcGIS Pro.

### `uncovered_areas.py`

Este script identifica las manzanas (áreas de la ciudad) que no están cubiertas por la zona de influencia de las áreas verdes y exporta esta información a una nueva capa.

- **Parámetros de Entrada**:
  - `fcIn`: La capa de entrada que contiene las manzanas de la ciudad que se analizarán.
  - `fcIn2`: La capa que contiene el buffer de cobertura actual de las áreas verdes.
  - `dirOut`: El directorio de salida donde se almacenará el resultado.
  - `nameOut`: El nombre del archivo resultante que contendrá las manzanas no cubiertas.

- **Uso**:
  1. Abre ArcGIS Pro y asegúrate de que el proyecto actual está cargado.
  2. Corre el script con los parámetros necesarios. Ejemplo en Python:
     ```python
     import arcpy

     def script_tool(fcIn, fcIn2, dirOut, nameOut):
         return

     if __name__ == "__main__":
         fcIn = arcpy.GetParameterAsText(0)
         fcIn2 = arcpy.GetParameterAsText(1)
         dirOut = arcpy.GetParameterAsText(2)
         nameOut = arcpy.GetParameterAsText(3)

         script_tool(fcIn, fcIn2, dirOut, nameOut)
         arcpy.SetParameterAsText(3, "Result")

     # DEFINIR ENTORNO
     aprx = arcpy.mp.ArcGISProject("CURRENT")

     # SE AGREGA CAPAS DE CONTENIDO
     aprxMap = aprx.listMaps()[0]
     aprxMap.addDataFromPath(fcIn) # Manzanas No cubiertas
     aprxMap.addDataFromPath(fcIn2) # Buffer de cobertura actual de las áreas verdes
     content = []
     n = len(aprxMap.listLayers())
     for i in list(range(0,n)):
         content.append(aprxMap.listLayers()[i].name)

     arcpy.AddMessage("Se iniciaron los parámetros de entrada")

     # GEO PROCESO
     fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida
     # Seleccionar manzanas que no intersectan con el buffer
     arcpy.management.SelectLayerByLocation(content[1], "INTERSECT", content[0], None, "NEW_SELECTION", "INVERT")

     # Exportar la selección a una nueva capa
     arcpy.management.CopyFeatures(content[1], fcOut)

     # Limpiar selección
     arcpy.management.SelectLayerByAttribute(content[1], 'CLEAR_SELECTION')
     arcpy.AddMessage("Producto final obtenido")

     # AGREGAR RESULTADO A LA TABLA DE CONTENIDO
     aprxMap.addDataFromPath(fcOut)
     ```

- **Resultado**: El script genera un archivo de salida que contiene las manzanas no cubiertas por la zona de influencia de las áreas verdes y lo añade al proyecto.

  paso 3
  ## Instalación

Para ejecutar este proyecto, sigue los siguientes pasos:

1. **Requisitos previos**:
   - Debes tener instalado ArcGIS Pro en tu computadora.
   
2. **Pasos**:
   1. Clona este repositorio en tu máquina local:
      ```bash
      git clone https://github.com/tu-usuario/nombre-repositorio.git
      ```
   2. Abre ArcGIS Pro y carga los archivos de proyecto del repositorio clonado.
   3. Sigue las instrucciones específicas de cada código para ejecutar las diferentes etapas del análisis.

## Uso

El proyecto está compuesto por varios scripts independientes que se ejecutan secuencialmente para alcanzar el análisis final. Cada script tiene un propósito específico:

### `create_buffer.py`

Este script genera una zona de influencia (buffer) de 400 metros alrededor de las áreas verdes especificadas en la comuna de La Cisterna.

- **Parámetros de Entrada**:
  - `fcIn`: La capa de entrada que contiene las áreas verdes.
  - `dirOut`: El directorio de salida donde se almacenará el resultado.
  - `nameOut`: El nombre del archivo resultante que contendrá la zona de influencia.

- **Uso**:
  1. Abre ArcGIS Pro y asegúrate de que el proyecto actual está cargado.
  2. Corre el script con los parámetros necesarios. Ejemplo en Python:
     ```python
     import arcpy

     def script_tool(fcIn, dirOut, nameOut):
         return

     if __name__ == "__main__":
         fcIn = arcpy.GetParameterAsText(0)  # Áreas verdes
         dirOut = arcpy.GetParameterAsText(1) # Directorio de salida
         nameOut = arcpy.GetParameterAsText(2) # Nombre de la zona de influencia (buffer)

         script_tool(fcIn, dirOut, nameOut)
         arcpy.SetParameterAsText(2, "Result")

     # DEFINIR ENTORNO
     aprx = arcpy.mp.ArcGISProject("CURRENT")
     aprxMap = aprx.listMaps()[0]
     arcpy.AddMessage("Se iniciaron los parámetros de entrada")

     # AGREGAR CAPAS DE CONTENIDO
     aprxMap.addDataFromPath(fcIn)
     content = []
     content.append(aprxMap.listLayers()[0].name)

     # GEO PROCESO
     fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida
     dist = "400"  # Estándar recomendado por INE
     distBuffer = f"{dist} Meters"
     
     arcpy.analysis.Buffer(fcIn, fcOut, distBuffer, "FULL", "ROUND", "ALL", None, "PLANAR")
     arcpy.AddMessage("Geo proceso terminado")

     # AGREGAR RESULTADO A LA TABLA DE CONTENIDO
     aprxMap.addDataFromPath(fcOut)
     ```

- **Resultado**: El script crea un archivo de salida que contiene la zona de influencia alrededor de las áreas verdes y lo añade al proyecto de ArcGIS Pro.

### `uncovered_areas.py`

Este script identifica las manzanas (áreas de la ciudad) que no están cubiertas por la zona de influencia de las áreas verdes y exporta esta información a una nueva capa.

- **Parámetros de Entrada**:
  - `fcIn`: La capa de entrada que contiene las manzanas de la ciudad que se analizarán.
  - `fcIn2`: La capa que contiene el buffer de cobertura actual de las áreas verdes.
  - `dirOut`: El directorio de salida donde se almacenará el resultado.
  - `nameOut`: El nombre del archivo resultante que contendrá las manzanas no cubiertas.

- **Uso**:
  1. Abre ArcGIS Pro y asegúrate de que el proyecto actual está cargado.
  2. Corre el script con los parámetros necesarios. Ejemplo en Python:
     ```python
     import arcpy

     def script_tool(fcIn, fcIn2, dirOut, nameOut):
         return

     if __name__ == "__main__":
         fcIn = arcpy.GetParameterAsText(0)
         fcIn2 = arcpy.GetParameterAsText(1)
         dirOut = arcpy.GetParameterAsText(2)
         nameOut = arcpy.GetParameterAsText(3)

         script_tool(fcIn, fcIn2, dirOut, nameOut)
         arcpy.SetParameterAsText(3, "Result")

     # DEFINIR ENTORNO
     aprx = arcpy.mp.ArcGISProject("CURRENT")

     # SE AGREGA CAPAS DE CONTENIDO
     aprxMap = aprx.listMaps()[0]
     aprxMap.addDataFromPath(fcIn) # Manzanas No cubiertas
     aprxMap.addDataFromPath(fcIn2) # Buffer de cobertura actual de las áreas verdes
     content = []
     n = len(aprxMap.listLayers())
     for i in list(range(0,n)):
         content.append(aprxMap.listLayers()[i].name)

     arcpy.AddMessage("Se iniciaron los parámetros de entrada")

     # GEO PROCESO
     fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida
     # Seleccionar manzanas que no intersectan con el buffer
     arcpy.management.SelectLayerByLocation(content[1], "INTERSECT", content[0], None, "NEW_SELECTION", "INVERT")

     # Exportar la selección a una nueva capa
     arcpy.management.CopyFeatures(content[1], fcOut)

     # Limpiar selección
     arcpy.management.SelectLayerByAttribute(content[1], 'CLEAR_SELECTION')
     arcpy.AddMessage("Producto final obtenido")

     # AGREGAR RESULTADO A LA TABLA DE CONTENIDO
     aprxMap.addDataFromPath(fcOut)
     ```

- **Resultado**: El script genera un archivo de salida que contiene las manzanas no cubiertas por la zona de influencia de las áreas verdes y lo añade al proyecto de ArcGIS Pro.

### `create_new_buffer.py`

Este script genera una nueva zona de influencia (buffer) de 400 metros alrededor de las manzanas que no están cubiertas por la zona de influencia de las áreas verdes existentes.

- **Parámetros de Entrada**:
  - `fcIn`: La capa de entrada que contiene las manzanas no cubiertas por la zona de influencia de las áreas verdes existentes.
  - `dirOut`: El directorio de salida donde se almacenará el resultado.
  - `nameOut`: El nombre del archivo resultante que contendrá la nueva zona de influencia.

- **Uso**:
  1. Abre ArcGIS Pro y asegúrate de que el proyecto actual está cargado.
  2. Corre el script con los parámetros necesarios. Ejemplo en Python:
     ```python
     import arcpy

     def script_tool(fcIn, dirOut, nameOut):
         return

     if __name__ == "__main__":
         fcIn = arcpy.GetParameterAsText(0)  # Manzanas NO cubiertas por zona de influencia de las áreas verdes existentes
         dirOut = arcpy.GetParameterAsText(1) # Directorio de salida
         nameOut = arcpy.GetParameterAsText(2) # Nombre de la zona de influencia (buffer)

         script_tool(fcIn, dirOut, nameOut)
         arcpy.SetParameterAsText(2, "Result")

     # DEFINIR ENTORNO
     aprx = arcpy.mp.ArcGISProject("CURRENT")
     aprxMap = aprx.listMaps()[0]
     arcpy.AddMessage("Se iniciaron los parámetros de entrada")

     # AGREGAR CAPAS DE CONTENIDO
     aprxMap.addDataFromPath(fcIn)
     content = []
     content.append(aprxMap.listLayers()[0].name)

     # GEO PROCESO
     fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida
     dist = "400"  # Estándar recomendado por INE
     distBuffer = f"{dist} Meters"
     
     arcpy.analysis.Buffer(fcIn, fcOut, distBuffer, "FULL", "ROUND", "NONE", None, "PLANAR")
     arcpy.AddMessage("Geo proceso terminado")

     # AGREGAR RESULTADO A LA TABLA DE CONTENIDO
     aprxMap.addDataFromPath(fcOut)
     ```

- **Resultado**: El script crea un archivo de salida que contiene una nueva zona de influencia alrededor de las manzanas no cubiertas por las áreas verdes existentes y lo añade al proyecto de ArcGIS Pro.
paso 4

Genera una zona de influencia (buffer) de 400 metros alrededor de las áreas verdes existentes.

- **Parámetros de Entrada**:
  - `fcIn`: Capa de entrada con las áreas verdes.
  - `dirOut`: Directorio de salida para los resultados.
  - `nameOut`: Nombre del archivo de salida.

- **Uso**:
  Ejecutar en ArcGIS Pro proporcionando las capas y directorios correspondientes.

### `uncovered_areas.py`

Identifica las manzanas no cubiertas por la zona de influencia de las áreas verdes y exporta esta información a una nueva capa.

- **Parámetros de Entrada**:
  - `fcIn`: Capa con las manzanas de la ciudad.
  - `fcIn2`: Capa con el buffer de cobertura actual de áreas verdes.
  - `dirOut`: Directorio de salida para los resultados.
  - `nameOut`: Nombre del archivo de salida.

- **Uso**:
  Ejecutar en ArcGIS Pro proporcionando las capas y directorios correspondientes.

### `create_new_buffer.py`

Genera una nueva zona de influencia de 400 metros alrededor de las manzanas no cubiertas por las áreas verdes existentes.

- **Parámetros de Entrada**:
  - `fcIn`: Capa con las manzanas no cubiertas.
  - `dirOut`: Directorio de salida para los resultados.
  - `nameOut`: Nombre del archivo de salida.

- **Uso**:
  Ejecutar en ArcGIS Pro proporcionando las capas y directorios correspondientes.

### `optimal_areas.py`

Este script selecciona las manzanas óptimas para la creación de nuevas áreas verdes, priorizando aquellas que cubren la mayor área no cubierta actualmente. Luego, exporta esta selección a una nueva capa.

- **Parámetros de Entrada**:
  - `fcIn`: Capa con las manzanas no cubiertas.
  - `fcIn2`: Capa con el buffer de manzanas no cubiertas.
  - `dirOut`: Directorio de salida para los resultados.
  - `nameOut`: Nombre del archivo de salida.

- **Uso**:
  1. Ejecutar el script en ArcGIS Pro proporcionando las capas y directorios correspondientes.
  2. El script seleccionará las manzanas óptimas y creará una nueva capa con estas selecciones.
     
paso 5

## Uso

### Parámetros de Entrada

1. **`fcIn`**: Capa de entrada con las manzanas óptimas para la creación de nuevas áreas verdes.
2. **`dirOut`**: Directorio donde se guardará el archivo de salida.
3. **`nameOut`**: Nombre del archivo de salida que contendrá el buffer generado.

### Ejecución

Para ejecutar el script en ArcGIS Pro:
1. Proporciona la capa de entrada (`fcIn`).
2. Especifica el directorio de salida (`dirOut`).
3. Asigna un nombre al archivo de salida (`nameOut`).

El script realiza las siguientes acciones:
1. **Configuración**: Inicia el proyecto actual en ArcGIS Pro y selecciona el primer mapa disponible.
2. **Adición de Capa**: Agrega la capa de manzanas óptimas al mapa.
3. **Generación de Buffer**: Crea un buffer de 400 metros alrededor de las manzanas óptimas.
4. **Visualización**: Agrega el buffer generado al mapa para su análisis.

### Código del Script

```python
import arcpy

def script_tool(fcIn, dirOut, nameOut):
    """Script code goes below"""
    return

if __name__ == "__main__":
    fcIn = arcpy.GetParameterAsText(0)  # Manzanas Optimas para un AR
    dirOut = arcpy.GetParameterAsText(1) # Directorio salida
    nameOut = arcpy.GetParameterAsText(2) # Nombre de la zona de influencia (buffer)

    script_tool(fcIn, dirOut, nameOut)
    arcpy.SetParameterAsText(2, "Result")

#----------------------------------------
# DEFINIR ENTORNO
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]

arcpy.AddMessage("Se iniciaron los parámetros de entrada")

# SE AGREGA CAPAS DE CONTENIDO
aprxMap.addDataFromPath(fcIn)
content = []
content.append(aprxMap.listLayers()[0].name)

# GEO PROCESO
fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida
dist = "400"  # estándar recomendado por INE
distBuffer = f"{dist} Meters"

arcpy.analysis.Buffer(fcIn, fcOut, distBuffer, "FULL", "ROUND", "ALL", None, "PLANAR")

arcpy.AddMessage("Geo proceso finalizado")

# AGREGAR RESULTADO A LA TABLA DE CONTENIDO
aprxMap.addDataFromPath(fcOut)

paso 6
## Uso

### Parámetros de Entrada

1. **`fcParquesPlazas`**: Capa de parques y plazas.
2. **`fcTablaCalidad`**: Tabla que contiene la información de calidad asociada a los parques y plazas.

### Ejecución

Para ejecutar el script en ArcGIS Pro:
1. Proporciona la capa de parques y plazas (`fcParquesPlazas`).
2. Especifica la tabla de calidad (`fcTablaCalidad`).

El script realiza las siguientes acciones:
1. **Configuración**: Carga la capa de parques y plazas y la tabla de calidad en el primer mapa disponible del proyecto actual de ArcGIS Pro.
2. **Unión de Campos**: Une la tabla de calidad a la capa de parques y plazas utilizando el campo `NOMBRE_EP` como clave común.
3. **Guardado del Proyecto**: Guarda los cambios realizados en el proyecto de ArcGIS Pro.

### Código del Script

```python
import arcpy

def script_tool(fcParquesPlazas, fcTablaCalidad):
    # Definir el campo común para la unión
    campo_comun = "NOMBRE_EP"
    
    try:
        # Añadir la capa de parques y plazas al proyecto (si no está añadida)
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        aprxMap = aprx.listMaps()[0]  # Seleccionar el primer mapa en el proyecto

        if not any(lyr.name == fcParquesPlazas for lyr in aprxMap.listLayers()):
            aprxMap.addDataFromPath(fcParquesPlazas)
        
        # Añadir la tabla de calidad al proyecto (si no está añadida)
        if not any(tbl.name == fcTablaCalidad for tbl in aprxMap.listTables()):
            aprxMap.addDataFromPath(fcTablaCalidad)
        
        arcpy.AddMessage("Realizando la unión de la tabla de calidad a la capa de parques y plazas...")

        # Realizar la unión de campos
        arcpy.management.JoinField(fcParquesPlazas, campo_comun, fcTablaCalidad, campo_comun)

        arcpy.AddMessage("Unión realizada con éxito.")

        # Guardar el proyecto
        aprx.save()
        arcpy.AddMessage("Proyecto guardado.")

    except arcpy.ExecuteError:
        arcpy.AddError(f"Error de ejecución en ArcPy: {arcpy.GetMessages(2)}")
    except Exception as e:
        arcpy.AddError(f"Error: {str(e)}")

if __name__ == "__main__":

    # Parámetros de entrada
    fcParquesPlazas = arcpy.GetParameterAsText(0)  # Capa de parques y plazas
    fcTablaCalidad = arcpy.GetParameterAsText(1)  # Tabla de calidad

    # Llamar a la función principal
    script_tool(fcParquesPlazas, fcTablaCalidad)

arcpy.AddMessage("Union de tabla a capa realizado")

paso 7
## Uso

### Parámetros de Entrada

1. **`fcIn`**: Capa de entrada que contiene las áreas verdes (parques y plazas).
2. **`dirOut`**: Directorio de salida donde se guardará la capa resultante.
3. **`nameOut`**: Nombre del archivo de salida para las áreas verdes propuestas para mejoramiento.

### Ejecución

Para ejecutar el script en ArcGIS Pro:
1. Proporciona la capa de entrada con las áreas verdes (`fcIn`).
2. Especifica el directorio de salida (`dirOut`).
3. Asigna un nombre para el archivo de salida (`nameOut`).

El script realiza las siguientes acciones:
1. **Configuración**: Carga la capa de áreas verdes en el primer mapa disponible del proyecto actual de ArcGIS Pro.
2. **Selección por Atributos**: Selecciona las áreas verdes que tienen un `RANGO INFERIOR` en el campo `RANGO_CALI`.
3. **Exportación**: Exporta las entidades seleccionadas a una nueva capa en el directorio especificado.
4. **Limpieza**: Limpia la selección actual en la capa.
5. **Añadir al Mapa**: Añade la nueva capa de salida al mapa.

### Código del Script

```python
import arcpy

def script_tool(fcIn, dirOut, nameOut):
    """Script code goes below"""

    return

if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)  # Areas verdes
    dirOut = arcpy.GetParameterAsText(1) # Directorio salida
    nameOut = arcpy.GetParameterAsText(2) # Areas verdes propuestas para mejoramiento

    script_tool(fcIn, dirOut, nameOut)
    arcpy.SetParameterAsText(2, "Result")

#----------------------------------------
# DEFINIR ENTORNO
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]

arcpy.AddMessage("Se iniciaron los parámetros de entrada")

# SE AGREGA CAPAS DE CONTENIDO
aprxMap.addDataFromPath(fcIn)
content = []
content.append(aprxMap.listLayers()[0].name)

# GEO PROCESO
fcOut = f"{dirOut}\\{str(nameOut)}" # Ruta completa del archivo de salida

# Crear una selección por atributo: seleccionar los parques y plazas con 'RANGO INFERIOR' en 'RANGO_CALI'
arcpy.AddMessage("Seleccionando parques y plazas con 'RANGO INFERIOR' en 'RANGO_CALI'...")
where_clause = "RANGO_CALI = 'RANGO INFERIOR'"

# Verificar si la capa de entrada ya es una capa de selección, si no, convertirla
if arcpy.Describe(fcIn).dataType != "FeatureLayer":
    fcParquesPlazas = arcpy.management.MakeFeatureLayer(fcIn, "parques_plazas_lyr").getOutput(0)

# Seleccionar las entidades que cumplen con la condición
arcpy.management.SelectLayerByAttribute(fcParquesPlazas, "NEW_SELECTION", where_clause)

# Exportar la selección a una nueva capa
arcpy.AddMessage(f"Exportando la selección a la nueva capa de salida en {fcOut}...")
arcpy.management.CopyFeatures(fcParquesPlazas, fcOut)

arcpy.AddMessage("Exportación completada.")

# Limpiar la selección
arcpy.management.SelectLayerByAttribute(fcParquesPlazas, 'CLEAR_SELECTION')
arcpy.AddMessage("Selección limpiada.")

# Añadir la nueva capa de salida al mapa
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcOut)

