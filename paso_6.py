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
