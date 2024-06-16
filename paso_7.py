
import arcpy


def script_tool(fcIn, dirOut, nameOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)  #Areas verdes
    dirOut = arcpy.GetParameterAsText(1) #Directorio salida
    nameOut = arcpy.GetParameterAsText(2) #Areas verdes propuestas para mejoramiento

    script_tool(fcIn, dirOut, nameOut)
    arcpy.SetParameterAsText(2, "Result")

#----------------------------------------
#DEFINIR ENTORNO
aprx = arcpy.mp.ArcGISProject("CURRENT")

aprxMap = aprx.listMaps()[0]

arcpy.AddMessage("Se iniciaron los parámetros de entrada")

#SE AGREGA CAPAS DE CONTENIDO
aprxMap.addDataFromPath(fcIn)
content = []
content.append(aprxMap.listLayers()[0].name)

#GEO PROCESO
fcOut = f"{dirOut}\\{str(nameOut)}" #Ruta completa del archivo de salida
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
#-----------------------------------------
# fcOut = f"{dirOut}\\{str(nameOut)}" #Ruta completa del archivo de salida

# # Identificación de áreas con equipamiento insuficiente
# #equipamiento_insuficiente = '"RANGO_CALI" = \'RANGO INFERIOR\''

# #propuesta ar insuficiente
# arcpy.management.SelectLayerByAttribute(
#     content[0],
#     "NEW_SELECTION",
#     "RANGO_CALI = 'RANGO INFERIOR'",
#     None
# )
# arcpy.AddMessage("cualquiercosa")

# # Crear la capa de puntos con el sistema de referencia espacial correspondiente (EPSG: 4326)
# centroide=arcpy.management.FeatureToPoint(
#     content[0],
#     fcOut,
#     point_location="CENTROID"
# )
# #--Exportar la selección a una nueva capa
# arcpy.management.CopyFeatures(content[0], fcOut)

# #Limpiar seleccion
# arcpy.management.SelectLayerByAttribute(content[1],'CLEAR_SELECTION')

# aprxMap.addDataFromPath(fcOut)-----------------------
# # Análisis espacial para decidir dónde se deben mejorar las áreas verdes
# # Crear una lista para almacenar los centroides únicos
# centroides = []
# with arcpy.da.SearchCursor(fcEquipamientoInsuf, ["SHAPE@"]) as cursor:
#     for row in cursor:
#     # Obtener la geometría del polígono
#         shape = row[0]
#         # Calcular el centroide del polígono
#         centroide = shape.centroid
#         # Verificar si el centroide ya ha sido registrado
#         if centroide not in centroides:
#             # Agregar el centroide a la lista de centroides
#             centroides.append(centroide)
#             # Insertar el centroide como un nuevo punto en la capa de propuesta de puntos
#             with arcpy.da.InsertCursor(nameOut, ["SHAPE@"]) as insert_cursor:
#                 insert_cursor.insertRow([centroide])

# arcpy.AddMessage("Puntos propuestos creados para mejoras de áreas verdes.")

# # Calcular la geometría de los puntos creados (por ejemplo, las coordenadas X e Y)
# arcpy.management.CalculateGeometryAttributes(nameOut, [["X_COORD", "POINT_X"], ["Y_COORD", "POINT_Y"]])


# # Eliminar capas temporales si es necesario
# if arcpy.Exists("equipamiento_insuf"):
#     arcpy.management.Delete("equipamiento_insuf")

# #AGREGAR RESULTADO A LA TABLA DE CONTENIDO
# aprxMap.addDataFromPath(nameOut)