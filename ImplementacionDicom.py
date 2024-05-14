import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pydicom 
import nibabel as nib
from ClasesDicom import *

print("******************BIENVENID@ AL SISTEMA DE GESTIÓN DE ARCHIVOS DICOM PNG Y JPG******************")
while True:
    menu=int(input("""Seleccione: 
         1. Agregar Paciente
         2. Ingresar Imagen jpg ó png
         3. Rotación Imagen Asociada Al Paciente
         4. Gestión Y Manipulación Imagen jpg ó png
         5.Salir Del Sistema 
         >>>> """))
    if menu == 1:
        a=Paciente()
        rutaDICOM=input("Ingrese por favor la ruta del archivo DICOM que relaciona al paciente >>> ")
        claveDICOM=input("Adicional a lo anterior, Ingrese una clave para guardar este archivo DICOM >>> ")
        a.leerDicom(claveDICOM,rutaDICOM)
        mostrar=a.agregarAtributos(claveDICOM)
        print(mostrar)
        print(" *** PACIENTE ALMACENADO CORRECTAMENTE *** ")
    elif menu == 2:
        b=JpgPng()
        ruta=input("Ingrese por favor la ruta de la imagen jpg ó png >>> ")
        clave=input("Adicional a lo anterior, Ingrese una clave para guardar esta imagen >>> ")
        b.leerImagen(clave,ruta)
        print(" *** IMAGEN ALMACENADA CORRECTAMENTE *** ")
    elif menu == 3:
        a=Paciente()
        bandera = False
        while not bandera: 
            ID = input("""Ingrese por favor la identificación del paciente 
                    (TENGA EN CUENTA QUE DICHA IDENTIFICACIÓN SE MOSTRÓ CUANDO SE REGISTRÓ EL PACIENTE) >>> """)
            if a.rotacion(ID) != "¡¡¡ Clave no encontrada en el sistema !!!":
                bandera = True
                break
            else:
                print("¡¡¡La clave es incorrecta, vuelva a intentar!!!")
                plt.close()
                break      
    elif menu == 4:
        b = JpgPng()
        bandera = False
        while not bandera:
            clave = input("Ingrese por favor la clave con la que se almacenó la imagen jpg ó png >>> ")
            if b.transformacion(clave) != "¡¡¡ Clave no encontrada en el sistema !!!":
                bandera = True 
                break
            else:
                print("¡¡¡La clave es incorrecta, vuelva a intentar!!!")
                plt.close()
                break
    elif menu == 5:
        print("¡¡¡ Usted ha salido exitosamente del sistema !!!")
        break
    else:
        print("¡¡¡¡ Opción no valida, vuelva a intentarlo !!!!")
        continue



