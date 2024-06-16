
import arcpy


def script_tool(fcIn, fcIn2, dirOut, nameOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0) #Manzanas No cubiertas
    fcIn2 = arcpy.GetParameterAsText(1) #Buffer de manzanas no cubiertas
    dirOut = arcpy.GetParameterAsText(2) #Directorio de salida
    nameOut = arcpy.GetParameterAsText(3) #Nombre de salida

    script_tool(fcIn, fcIn2, dirOut, nameOut)
    arcpy.SetParameterAsText(3, "Result")

#----------------------

#DEFINIR ENTORNO
aprx = arcpy.mp.ArcGISProject("CURRENT")


#SE AGREGA CAPAS DE CONTENIDO
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn)
aprxMap.addDataFromPath(fcIn2)
content = []
n = len(aprxMap.listLayers())
for i in list(range(0,n)):
    content.append(aprxMap.listLayers()[i].name)

arcpy.AddMessage("Se iniciaron los parámetros de entrada")

#GEO PROCESO
fcOut = f"{dirOut}\{str(nameOut)}" #Ruta completa del archivo de salida

# Crear un diccionario para almacenar las áreas cubiertas de las manzanas
areas_manzanas = {}

try:
    # Verificar si la capa de buffers existe
    if not arcpy.Exists(fcIn2):
        raise Exception(f"La capa de buffers {fcIn2} no existe.")
    
    # Calcular el área de cada parte de manzana dentro del buffer
    with arcpy.da.SearchCursor(fcIn2, ["OBJECTID", "SHAPE@", "MANZENT_I"]) as cursor:
        for row in cursor:
            OBJECTID, buffer_shape, MANZENT_I = row
            buffer_area = buffer_shape.area  # Calcular el área del polígono del buffer
            
            # Si la manzana no está en el diccionario, inicializarla
            if MANZENT_I not in areas_manzanas:
                areas_manzanas[MANZENT_I] = 0
            
            # Agregar el área del buffer a la manzana correspondiente
            areas_manzanas[MANZENT_I] += buffer_area

    # Ordenar las manzanas por área cubierta en orden descendente
    manzanas_ordenadas = sorted(areas_manzanas.items(), key=lambda x: x[1], reverse=True)
    
    manzanas_optimas_ids = []  # Lista para almacenar los IDs de las manzanas óptimas seleccionadas
    manzanas_ya_cubiertas = set()  # Conjunto para almacenar las manzanas que ya están cubiertas

    # Crear una capa temporal para las manzanas
    if arcpy.Exists("manzanas_lyr"):
        arcpy.management.Delete("manzanas_lyr")
    arcpy.management.MakeFeatureLayer(fcIn, "manzanas_lyr")

    for manzana_id, area in manzanas_ordenadas:
        if manzana_id not in manzanas_ya_cubiertas:
            # Añadir la manzana actual a la lista de manzanas óptimas
            manzanas_optimas_ids.append(manzana_id)
            
            # Crear una capa temporal específica para el buffer actual
            buffer_layer_name = f"buffer_lyr_{manzana_id}"
            if arcpy.Exists(buffer_layer_name):
                arcpy.management.Delete(buffer_layer_name)
            arcpy.management.MakeFeatureLayer(fcIn2, buffer_layer_name, f"MANZENT_I = '{manzana_id}'")

            # Seleccionar todas las manzanas que intersectan con este buffer
            arcpy.management.SelectLayerByLocation("manzanas_lyr", "INTERSECT", buffer_layer_name)
            
            # Obtener los IDs de las manzanas cubiertas
            covered_manzanas = [row[0] for row in arcpy.da.SearchCursor("manzanas_lyr", ["MANZENT_I"])]
            manzanas_ya_cubiertas.update(covered_manzanas)

            # Limpiar la capa temporal del buffer
            arcpy.management.Delete(buffer_layer_name)

    print(f"Las manzanas óptimas son: {manzanas_optimas_ids}")

    # Crear una nueva capa con las manzanas óptimas
    # Asegurarse de que la capa de salida no exista
    if arcpy.Exists(fcOut):
        arcpy.management.Delete(fcOut)
    
    # Seleccionar las manzanas óptimas en la capa de selección
    manzanas_optimas_ids_str = ", ".join([f"'{id}'" for id in manzanas_optimas_ids])
    seleccion_query = f"MANZENT_I IN ({manzanas_optimas_ids_str})"
    arcpy.management.SelectLayerByAttribute("manzanas_lyr", "NEW_SELECTION", seleccion_query)

    # Copiar las manzanas seleccionadas a una nueva clase de entidad
    arcpy.management.CopyFeatures("manzanas_lyr", fcOut)

    print(f"Las manzanas óptimas han sido guardadas en {fcOut}.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Cerrar cualquier capa temporal creada
    if arcpy.Exists("manzanas_lyr"):
        arcpy.management.Delete("manzanas_lyr")

arcpy.AddMessage("Analisis para determinar manzanas optimas finalizado")
#AGREGAR RESULTADO A LA TABLA DE CONTENIDO
aprxMap.addDataFromPath(fcOut)