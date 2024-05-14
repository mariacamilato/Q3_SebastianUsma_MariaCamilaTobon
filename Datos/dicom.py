import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pydicom 
import nibabel as nib 

paciente={}
dicomIm={}

class Paciente:
    def __init__(self, nombre="", edad="", ID="", imagen=""):
        self.nombre = nombre
        self.edad = edad
        self.ID = ID
        self.imagen = imagen
    
    def leerDicom(self,clave,ruta):
        leido=pydicom.dcmread(ruta)
        dicomIm[clave]=leido
    
def agregarAtributos(claveDICOM):
    for i in dicomIm:
        if i == claveDICOM:
            nombre=dicomIm[i][0x0010 , 0x0010].value #etiqueta del nombre
            edad=dicomIm[i][0x0010 , 0x1010].value #etiqueta edad
            ID=dicomIm[i][0x0010 , 0x0020].value #etiqueta ID
            imagen=dicomIm[i].pixel_array #etiqueta de imagen
            imagen_nifti = nib.Nifti1Image(imagen, affine=None)
            ruta_nifti = f"Nifti/{claveDICOM}.nii"  #ruta completa con el nombre del archivo NIfTI
            nib.save(imagen_nifti, ruta_nifti)
            a=Paciente(nombre,edad,ID,imagen)
            paciente[ID]=a #que en el diccionario de pacientes la clave asociada al paciente sea su ID
            return ID
        else:
            return "¡¡¡ Clave  encontrada en el sistema !!!"

def rotacion(ID):
    for i in paciente:
        if i == ID:
            matriz_imagen=paciente[i].imagen #atributo del objeto paciente
            height, width = matriz_imagen.shape[:2] 
            center=(width // 2, height // 2)  # Calcula el centro de la imagen
            scale = 1.0  # Escala de la imagen resultante
            while True:
                angulo=int(input("""Ingrese el ángulo de rotación para la imagen >>>
                            > 90
                            > 180
                            > 270 >>> """)) # Ángulo de rotación
                if angulo == 90:
                    rota = cv2.getRotationMatrix2D(center, angulo, scale) 
                    aplicacion = cv2.warpAffine(matriz_imagen, rota, (height, width))
                    plt.figure(figsize=(15,8),facecolor="lightblue")
                    plt.subplot(1,2,1)
                    plt.imshow(matriz_imagen,cmap="gray")
                    plt.title("IMAGEN ORIGINAL")
                    plt.subplot(1,2,2)
                    plt.imshow(aplicacion,cmap="gray")
                    plt.title(f"IMAGEN ROTADA {angulo} GRADOS")
                    plt.show()
                elif angulo == 180:
                    rota = cv2.getRotationMatrix2D(center, angulo, scale) 
                    aplicacion = cv2.warpAffine(matriz_imagen, rota, (height, width))
                    plt.figure(figsize=(15,8),facecolor="lightblue")
                    plt.subplot(1,2,1)
                    plt.imshow(matriz_imagen,cmap="gray")
                    plt.title("IMAGEN ORIGINAL")
                    plt.subplot(1,2,2)
                    plt.imshow(aplicacion,cmap="gray")
                    plt.title(f"IMAGEN ROTADA {angulo} GRADOS")
                    plt.show()
                elif angulo == 270:
                    rota = cv2.getRotationMatrix2D(center, angulo, scale) 
                    aplicacion = cv2.warpAffine(matriz_imagen, rota, (height, width))
                    plt.figure(figsize=(15,8),facecolor="lightblue")
                    plt.subplot(1,2,1)
                    plt.imshow(matriz_imagen,cmap="gray")
                    plt.title("IMAGEN ORIGINAL")
                    plt.subplot(1,2,2)
                    plt.imshow(aplicacion,cmap="gray")
                    plt.title(f"IMAGEN ROTADA {angulo} GRADOS")
                    plt.show()
                else:
                    print("¡¡¡ OPCIÓN NO VALIDA, INGRESE ÁNGULO DE 90° - 180° - 270° !!!")
                    continue
    else:
        return "¡¡¡ Clave  encontrada en el sistema !!!"

class JpgPng:
    def __init__(self, ruta=""):
        self.ruta = ruta
    
    def leerImagen(self,clave,ruta):
        imagen=cv2.imread(ruta)
        dicomIm[clave]=imagen
    
    def transformacion(self,clave):
        for i in dicomIm:
            if i == clave:
                imagen=cv2.cvtColor(dicomIm[i], cv2.COLOR_BGR2RGB) #IMAGEN ORIGINAL
                gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) #PONER EN ESCALA DE GRISES
                media=np.mean(imagen) #CALCULAR LA MEDIA PARA UN MEJOR UMBRAL DE LA IMAGEN
                Umb,imgB=cv2.threshold(gris,media,255,cv2.THRESH_TOZERO) #BINARIZAR
                x=int(input("Ingrese el primer valor para la dimensión del Kernel >>> "))
                y=int(input("Ingrese el segundo valor para la dimensión del Kernel >>> "))
                kernel = np.ones((x,y),np.uint8) #KERNEL
                tmorfolog=cv2.dilate(imgB,kernel,iterations = 1)
                tmorfolog=cv2.erode(tmorfolog,kernel,iterations = 1) #TRANSFORMACIÓN MORFOLÓGICA 
                plt.figure(figsize=(15,8),facecolor="lightblue")
                plt.subplot(2,2,1)
                plt.imshow(imagen, cmap='gray')
                plt.title("IMAGEN ORIGINAL")
                plt.subplot(2,2,2)
                plt.imshow(gris, cmap='gray')
                plt.title("IMAGEN EN ESCALA DE GRISES")
                plt.subplot(2,2,3)
                plt.imshow(imgB, cmap='gray')
                plt.title("IMAGEN BINARIZADA")
                plt.subplot(2,2,4)
                plt.imshow(tmorfolog, cmap="gray")
                plt.title("IMAGEN TRANSFORMACIONES MORFOLÓGICAS")
                plt.show()
            else:
                 return "¡¡¡ Clave  encontrada en el sistema !!!"



#---------------------------------------------------------------------------#
#PRUEBAS--------------------------------------------------------------------#

#b = Paciente()       
#b.leerDicom("123","Datos/000000.dcm")
#mostrar=agregarAtributos("123")
#mostrar1=rotacion("C3N-00247")
#print(mostrar)
b=JpgPng()
b.leerImagen("123","ImagenCelula.jpg")
b.transformacion("123")


                

    
    
    
    
    
