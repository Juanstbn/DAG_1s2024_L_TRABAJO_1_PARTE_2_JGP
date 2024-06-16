
import arcpy


def script_tool(fcIn, dirOut, nameOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)  #Manzanas Optimas para un AR
    dirOut = arcpy.GetParameterAsText(1) #Directorio salida
    nameOut = arcpy.GetParameterAsText(2) #Nombre de la zona de influencia (buffer)

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
fcOut = f"{dirOut}\{str(nameOut)}" #Ruta completa del archivo de salida
dist = "400"  #estandar recomendado por INE
distBuffer = f"{dist} Meters"

arcpy.analysis.Buffer(fcIn, fcOut, distBuffer, "FULL", "ROUND","ALL", None, "PLANAR")

arcpy.AddMessage("Geo proceso finalizado")

#AGREGAR RESULTADO A LA TABLA DE CONTENIDO
aprxMap.addDataFromPath(fcOut)