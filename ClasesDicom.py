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
    
    def agregarAtributos(self, claveDICOM):
        for clave, valor in dicomIm.items():  
            if clave == claveDICOM:
                nombre = valor[0x0010, 0x0010].value  
                edad = valor[0x0010, 0x1010].value  
                ID = valor[0x0010, 0x0020].value 
                imagen = valor.pixel_array  
                imagen_nifti = nib.Nifti1Image(imagen, affine=None)
                ruta_nifti = f"Nifti/{claveDICOM}.nii"  
                nib.save(imagen_nifti, ruta_nifti)
                paciente[ID] = Paciente(nombre, edad, ID, imagen)  
                return f"Nombre del paciente: {nombre}, Edad: {edad}, Identificación: {ID}"
        return None 

    def rotacion(self,ID):
        for i in paciente:
            if i == ID:
                matriz_imagen=paciente[i].imagen 
                height, width = matriz_imagen.shape[:2] 
                center=(width // 2, height // 2)  
                scale = 1.0  
                while True:
                    angulo=int(input("""Ingrese el ángulo de rotación para la imagen >>>
                                > 90
                                > 180
                                > 270 >>> """))
                    if angulo == 90:
                        rota = cv2.getRotationMatrix2D(center, angulo, scale) 
                        aplicacion = cv2.warpAffine(matriz_imagen, rota, (height, width))
                        imagen_normal=aplicacion/np.max(aplicacion)
                        valor=imagen_normal*255
                        aplicacion=valor.astype(np.uint8)
                        ruta_guardado = f"ImagenesModificadas/imagen_rotada_{angulo}.jpg"
                        cv2.imwrite(ruta_guardado, aplicacion) 
                        plt.figure(figsize=(15,8),facecolor="lightblue")
                        plt.subplot(1,2,1)
                        plt.imshow(matriz_imagen,cmap="gray")
                        plt.title("IMAGEN ORIGINAL")
                        plt.subplot(1,2,2)
                        plt.imshow(aplicacion,cmap="gray")
                        plt.title(f"IMAGEN ROTADA {angulo} GRADOS")
                        plt.show()
                        break
                    elif angulo == 180:
                        rota = cv2.getRotationMatrix2D(center, angulo, scale) 
                        aplicacion = cv2.warpAffine(matriz_imagen, rota, (height, width))
                        imagen_normal=aplicacion/np.max(aplicacion)
                        valor=imagen_normal*255
                        aplicacion=valor.astype(np.uint8)
                        ruta_guardado = f"ImagenesModificadas/imagen_rotada_{angulo}.jpg"
                        cv2.imwrite(ruta_guardado, aplicacion) 
                        plt.figure(figsize=(15,8),facecolor="lightblue")
                        plt.subplot(1,2,1)
                        plt.imshow(matriz_imagen,cmap="gray")
                        plt.title("IMAGEN ORIGINAL")
                        plt.subplot(1,2,2)
                        plt.imshow(aplicacion,cmap="gray")
                        plt.title(f"IMAGEN ROTADA {angulo} GRADOS")
                        plt.show()
                        break
                    elif angulo == 270:
                        rota = cv2.getRotationMatrix2D(center, angulo, scale) 
                        aplicacion = cv2.warpAffine(matriz_imagen, rota, (height, width))
                        imagen_normal=aplicacion/np.max(aplicacion)
                        valor=imagen_normal*255
                        aplicacion=valor.astype(np.uint8)
                        ruta_guardado = f"ImagenesModificadas/imagen_rotada_{angulo}.jpg"
                        cv2.imwrite(ruta_guardado, aplicacion) 
                        plt.figure(figsize=(15,8),facecolor="lightblue")
                        plt.subplot(1,2,1)
                        plt.imshow(matriz_imagen,cmap="gray")
                        plt.title("IMAGEN ORIGINAL")
                        plt.subplot(1,2,2)
                        plt.imshow(aplicacion,cmap="gray")
                        plt.title(f"IMAGEN ROTADA {angulo} GRADOS")
                        plt.show()
                        break
                    else:
                        print("¡¡¡ OPCIÓN NO VALIDA, INGRESE ÁNGULO DE 90° - 180° - 270° !!!")
                        continue
        else:
            return "¡¡¡ Clave no encontrada en el sistema !!!"

class JpgPng:
    def __init__(self, ruta=""):
        self.ruta = ruta
    
    def leerImagen(self,clave,ruta):
        imagen=cv2.imread(ruta)
        dicomIm[clave]=imagen
    
    def transformacion(self, clave):
        encontrado = False
        for i in dicomIm:
                if i == clave:
                    imagen = cv2.cvtColor(dicomIm[i], cv2.COLOR_BGR2RGB) 
                    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) 
                    media = np.mean(imagen) 
                    Umb, imgB = cv2.threshold(gris, media, 255, cv2.THRESH_TOZERO) 
                    x = int(input("Ingrese el primer valor para la dimensión del Kernel >>> "))
                    y = int(input("Ingrese el segundo valor para la dimensión del Kernel >>> "))
                    kernel = np.ones((x, y), np.uint8) 
                    tmorfolog = cv2.dilate(imgB, kernel, iterations=1)
                    tmorfolog = cv2.erode(tmorfolog, kernel, iterations=1)  
                    xt = cv2.putText(tmorfolog, f"IMAGEN BINARIZADA - KERNEL > {x,y} - UMBRAL {Umb}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) 
                    ruta_guardado = f"ImagenesModificadas/imagen_binarizada.jpg"
                    cv2.imwrite(ruta_guardado, xt) 
                    plt.figure(figsize=(15, 8), facecolor="lightblue")
                    plt.subplot(2, 2, 1)
                    plt.imshow(imagen, cmap='gray')
                    plt.title("IMAGEN ORIGINAL")
                    plt.subplot(2, 2, 2)
                    plt.imshow(gris, cmap='gray')
                    plt.title("IMAGEN EN ESCALA DE GRISES")
                    plt.subplot(2, 2, 3)
                    plt.imshow(imgB, cmap='gray')
                    plt.title("IMAGEN BINARIZADA")
                    plt.subplot(2, 2, 4)
                    plt.imshow(xt, cmap="gray")
                    plt.title("IMAGEN TRANSFORMACIONES MORFOLÓGICAS")
                    plt.show()
                    encontrado = True
                    break
        if not encontrado:
                return "¡¡¡ Clave no encontrada en el sistema !!!"



#---------------------------------------------------------------------------#
#PRUEBAS--------------------------------------------------------------------#

#b = Paciente()       
#b.leerDicom("123","Datos/000000.dcm")
#mostrar=agregarAtributos("123")
#mostrar1=rotacion("C3N-00247")
#print(mostrar)
#b=JpgPng()
#b.leerImagen("123","ImagenCelula.jpg")
#b.transformacion("123")


                

    
    
    
    
    
