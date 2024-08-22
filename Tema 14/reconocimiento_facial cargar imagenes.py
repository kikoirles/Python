# instalacion de visual estudi (https://visualstudio.microsoft.com/es/downloads/)
#                               Opcion Desarrollo para el escritorio con C++
# Bibliotecas al instalar ()
# cmake
# dlib
# face-recognition
# numpy
# opencv-python

from cv2 import cv2
import face_recognition

# cargar imagenes
foto_control = fr.load image-file('fotoA.jpg')
foto_prueba = fr.load image-file('fotoB.jpg')


# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar cara control
lugar_cara_A = fr.face_locations(foto_prueba)[0]
cara_codificada_A = fr.face_encodings(foto_prueba)[0]

# localizar cara prueba
lugar_cara_B = fr.face_locations(foto_control)[0]
cara_codificada_B = fr.face_encodings(foto_control)[0]


# mostrar rectangulo
cv2.rectangulo(foto_control,
               (lugar_cara_A[3], lugar_cara_A[0]),
               (lugar_cara_A[1], lugar_cara_A[2]),
               (0, 255, 0),
               2)

# mostrar rectangulo cara prueba
cv2.rectangulo(foto_prueba,
               (lugar_cara_B[3], lugar_cara_B[0]),
               (lugar_cara_B[1], lugar_cara_B[2]),
               (0, 255, 0),
               2)

# realizar comprarcion = True
resultado = fr.compare_faces(cara_codificada_A, cara_codificada_B)
print(resultado)

# medida de la distancia a 0,3 de tolerancia
distancia = fr.face_distancia([cara_codificada_A], cara_codificada_B,0.3)
print(distancia)

# mostrar resultado a nueva foto (prueba) a comprar con la foto control
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)


# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# mantener programa abierto
cv2.waitkey(0)