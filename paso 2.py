
import arcpy


def script_tool(fcIn, fcIn2, dirOut, nameOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)
    fcIn2 = arcpy.GetParameterAsText(1)
    dirOut = arcpy.GetParameterAsText(2)
    nameOut = arcpy.GetParameterAsText(3)

    script_tool(fcIn, fcIn2, dirOut, nameOut)
    arcpy.SetParameterAsText(3, "Result")

#----------------------

#DEFINIR ENTORNO
aprx = arcpy.mp.ArcGISProject("CURRENT")


#SE AGREGA CAPAS DE CONTENIDO
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn) #Manzanas No cubiertas
aprxMap.addDataFromPath(fcIn2) #Buffer de cobertura actual de las areas verdes
content = []
n = len(aprxMap.listLayers())
for i in list(range(0,n)):
    content.append(aprxMap.listLayers()[i].name)

arcpy.AddMessage("Se iniciaron los parámetros de entrada")

#GEO PROCESO
fcOut = f"{dirOut}\{str(nameOut)}" #Ruta completa del archivo de salida
#--Seleccionar manzanas que no intersectan con el buffer
arcpy.management.SelectLayerByLocation(content[1], "INTERSECT", content[0], None, "NEW_SELECTION", "INVERT")

#--Exportar la selección a una nueva capa
arcpy.management.CopyFeatures(content[1], fcOut)

#--Limpiar seleccion
arcpy.management.SelectLayerByAttribute(content[1],'CLEAR_SELECTION')
arcpy.AddMessage("Producto final obtenido")

#AGREGAR RESULTADO A LA TABLA DE CONTENIDO
aprxMap.addDataFromPath(fcOut)

