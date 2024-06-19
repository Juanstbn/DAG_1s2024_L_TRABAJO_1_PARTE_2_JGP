
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
